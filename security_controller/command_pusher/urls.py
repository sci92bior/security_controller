# urls for this views
from django.urls import path

from security_controller.command_pusher.views import get_switches, get_switch_details, get_flow_tables, add_flow_entry

urlpatterns = [
    path('switch/', get_switches, name='get_switches'),
    path('switch/<str:switch_id>', get_switch_details, name='get_switch_details'),
    path('switch/<str:switch_id>/flow_tables', get_flow_tables, name='get_flow_tables'),
    path('flow_entry/', add_flow_entry, name='add_flow_entry')
]