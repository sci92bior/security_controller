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


class VIPService(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True, blank=True)
    port = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
