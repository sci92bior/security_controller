from collections import defaultdict

from django.core.exceptions import ValidationError
from django.db import models

from security_controller.command_pusher.models import Switch, Match, Action, FlowEntry
from security_controller.common.models import TimestampedModel, ActionTypes, MatchTypes


class ConditionRule(models.Model):
    field_name = models.CharField(max_length=50, choices=MatchTypes.choices)
    value = models.CharField(max_length=50)


class PolicyRule(models.Model):
    match = models.CharField(max_length=50) # event or alert
    action = models.CharField(max_length=50, choices=ActionTypes.choices)
    conditions = models.ManyToManyField(ConditionRule)

    def __str__(self):
        return self.match + " " + self.action

    class Meta:
        verbose_name = "PolicyRule"
        verbose_name_plural = "PolicyRules"


class PolicyRecord(TimestampedModel):
    policy_id = models.CharField(max_length=50, unique=True)
    target = models.CharField(max_length=50)
    priority = models.IntegerField()
    rules = models.OneToOneField(PolicyRule, on_delete=models.CASCADE, null=True, blank=True, related_name='policyrecord')

    # po dodaniu polityki wyslij do wszystkich switchy wpisy do tebeli przeyplywu z polityka
    # po usunieciu polityki wyslij do wszystkich switchy usuniecie wpisow z tabeli przeyplywu z polityka
    # po zmianie polityki wyslij do wszystkich switchy zmiane wpisow z tabeli przeyplywu z polityka
    def save(self, *args, **kwargs):
        super().save()
        policy = PolicyRecord.objects.get(id=self.id)
        # convert rules in policy to match and action in flow entry
        for switch in Switch.objects.all():
            for rule in policy.rules.conditions.all():
                match = Match.objects.create(dl_dst=rule.value)
                action = Action.objects.create(type=policy.rules.action, port=policy.target)
                flow_entry = FlowEntry.objects.create(switch=switch, match=match, actions=action)
                flow_entry.save()








    def clean(self):
        # Check for collisions with other records
        collisions = self.detect_collisions_with_other_records()

        if collisions:
            raise ValidationError({
                'target': f"Policy collision detected for target '{self.target}'",
                'collisions': collisions,
            })

    def detect_collisions_with_other_records(self):
        # Create a dictionary to store condition rules by field name and value
        condition_rules_dict = defaultdict(list)

        # Iterate through the rules associated with this policy record
        for condition_rule in self.rules.conditions.all():
            condition_rules_dict[condition_rule.field_name].append(condition_rule.value)

        # Check for collisions by examining condition rules with multiple associated policies
        collisions = []

        # Get all other PolicyRecords
        other_records = PolicyRecord.objects.exclude(id=self.id)

        for other_record in other_records:
            for key, policies in condition_rules_dict.items():
                other_condition_rules = other_record.rules.filter(conditions__field_name=key[0],
                                                                  conditions__value=key[1])

                if other_condition_rules:
                    # Check if all conditions match for collision
                    if len(policies) == len(other_condition_rules):
                        collision = {
                            'condition_key': key,
                            'policies': policies,
                            'other_record': other_record,
                        }
                        collisions.append(collision)

        return collisions
