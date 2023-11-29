from collections import defaultdict

from security_controller.policy_resolver.models import PolicyRecord


def resolve_policy_collisions():
    # Get all PolicyRecords ordered by priority (highest priority first)
    policy_records = PolicyRecord.objects.order_by('-priority')

    # Create a dictionary to store policies by target
    target_policies = defaultdict(list)
    analysed_policies = []

    # Iterate through policy records and store them in the dictionary
    for policy_record in policy_records:
        target_policies[policy_record.target].append(policy_record)

    # Check for collisions within each target group
    for target, policies in target_policies.items():
        for i in range(len(policies)):
            for j in range(i + 1, len(policies)):
                policy1 = policies[i]
                policy2 = policies[j]

                collision_detected = False

                for rule1 in policy1.rules.all():
                    for rule2 in policy2.rules.all():
                        if rule1.field_name == rule2.field_name and rule1.value == rule2.value:
                            collision_detected = True
                            break

                if collision_detected:
                    print(f"Policy collision detected for target '{target}':")
                    print(f"Policy 1: {policy1.policy_id} (Priority {policy1.priority})")
                    print(f"Policy 2: {policy2.policy_id} (Priority {policy2.priority})")
                    print("Colliding Condition Rule(s):")
                    print(f"Field Name: {rule1.field_name}, Value: {rule1.value}")
                    print(f"Field Name: {rule2.field_name}, Value: {rule2.value}")
                    print("\n")

                    # If higher-priority policy has a collision, skip lower-priority one
                    if policy1.priority > policy2.priority:
                        policies[j] = None
                    else:
                        policies[i] = None

    # After resolving collisions, update the PolicyRecord objects
    for target, policies in target_policies.items():
        updated_policies = [policy for policy in policies if policy is not None]
        analysed_policies.extend(updated_policies)

        for i, policy in enumerate(updated_policies):
            policy.priority = i + 1  # Update the priority based on the new order
            policy.save()

    return analysed_policies


def implement_policy_on_nc():

    policies = resolve_policy_collisions()
    for policy in policies:
        translate_security_policy_to_ryu_flow(policy)


def translate_security_policy_to_ryu_flow(policy):
    data ={
        "dpid": policy.target,
        "priority": policy.priority,
        "match": policy.rules.conditions.all(),
        "actions":   [
            {
                "type": policy.rules.action
            }
        ] if policy.rules.action != "drop" else []
        }






