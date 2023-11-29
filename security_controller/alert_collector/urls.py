# urls for this views
from django.urls import path

from security_controller.alert_collector.views import add_alert
from security_controller.command_pusher.views import get_switches, get_switch_details, get_flow_tables, add_flow_entry

urlpatterns = [
    path('', add_alert, name='add_alert'),
]