from django.contrib import admin

from security_controller.command_pusher.models import Switch, FlowEntry


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    pass


@admin.register(FlowEntry)
class FlowEntryAdmin(admin.ModelAdmin):
    pass