from rest_framework import serializers

from security_controller.command_pusher.models import Match, Action, FlowEntry


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class CreateFlowEntrySerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True)
    match = MatchSerializer()
    dpid = serializers.IntegerField()

    class Meta:
        model = FlowEntry
        exclude = ('switch',)