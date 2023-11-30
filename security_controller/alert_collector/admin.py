from django.contrib import admin

from security_controller.alert_collector.models import VIPService, Alert


@admin.register(VIPService)
class VIPService(admin.ModelAdmin):
    pass


@admin.register(Alert)
class Alert(admin.ModelAdmin):
    readonly_fields = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')
    list_display = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')
    list_filter = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')
