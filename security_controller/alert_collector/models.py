from django.db import models


class Alert(models.Model):
    alert_type = models.CharField(max_length=50)
    device_ip = models.CharField(max_length=50)
    port = models.CharField(max_length=50)
    src_ip = models.CharField(max_length=50)
    dst_ip = models.CharField(max_length=50)
    alert_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alert_type

    def is_associated_with_vip_service(self):
        vip_services = VIPService.objects.all()
        for vip_service in vip_services:
            if vip_service.ip == self.src_ip or vip_service.ip == self.dst_ip:
                return True
        return False

    def is_duplicate(self):
        # additional check if same alert was received in last 30 seconds
        alerts = Alert.objects.all()
        for alert in alerts:
            if alert.alert_type == self.alert_type and alert.device_ip == self.device_ip and alert.port == self.port and alert.src_ip == self.src_ip and alert.dst_ip == self.dst_ip and alert.id != self.id:
                if (self.alert_time - alert.alert_time).seconds < 300:
                    return True
        return False


class VIPService(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True, blank=True)
    port = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
