from rest_framework import serializers

from security_controller.alert_collector.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'