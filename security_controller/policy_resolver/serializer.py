from rest_framework import serializers

from security_controller.policy_resolver.models import PolicyRecord, PolicyRule, ConditionRule, ActionTypes


class ConditionRuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConditionRule
        fields = '__all__'


class PolicyRuleSerializer(serializers.ModelSerializer):
    conditions = ConditionRuleSerializer(many=True)

    class Meta:
        model = PolicyRule
        fields = ['match', 'action', 'conditions']


class PolicySerializer(serializers.ModelSerializer):
    rules = PolicyRuleSerializer(many=True)

    class Meta:
        model = PolicyRecord
        fields = '__all__'