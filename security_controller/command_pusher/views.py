import json

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from security_controller.command_pusher.models import Switch, FlowEntry, Match, Action
from security_controller.command_pusher.serializers import MatchSerializer, CreateFlowEntrySerializer
from security_controller.command_pusher.services import RyuControllerService


@api_view(['GET'])
def get_switches(request):
    ryu_controller_service = RyuControllerService()
    response = ryu_controller_service.get_connected_switches()
    for switch_dpid in response:
        switch_data = ryu_controller_service.get_switch_details(switch_dpid)
        if Switch.objects.filter(dpid=switch_dpid).exists():
            Switch.objects.filter(dpid=switch_dpid).update(manufacturer=switch_data['mfr_desc'],
                                                           hardware=switch_data['hw_desc'],serial_number=switch_data['serial_num'],connected=True)
        else:
            Switch.objects.create(dpid=switch_dpid,manufacturer=switch_data['mfr_desc'],
                                  hardware=switch_data['hw_desc'],serial_number=switch_data['serial_num'],connected=True)

        get_flow_stats = ryu_controller_service.get_flow_stats(switch_dpid)
    return Response(response)


@api_view(['GET'])
def get_flow_tables(request, switch_id):
    switch = get_object_or_404(Switch, dpid=switch_id)
    ryu_controller_service = RyuControllerService()
    response = ryu_controller_service.get_flow_stats(switch_id)
    # delete all the flow entries for this switch
    FlowEntry.objects.filter(switch=switch).delete()
    for flow_entry in response:
        # delete all related match
        Match.objects.filter(flowentry__switch=switch).delete()
        match_serializer = MatchSerializer(data=flow_entry['match'])
        if match_serializer.is_valid():
            saved_match = match_serializer.save()
        else:
            return Response(match_serializer.errors)
        actions = []
        for action in flow_entry['actions']:
            type, port = action.split(':')
            if not Action.objects.filter(type=type, port=port).exists():
                action = Action.objects.create(type=type, port=port)
            else:
                action = Action.objects.get(type=type, port=port)
            actions.append(action)
        flow = FlowEntry.objects.create(switch=switch, duration_sec=flow_entry['duration_sec'],
                                    duration_nsec=flow_entry['duration_nsec'], priority=flow_entry['priority'],
                                    length=flow_entry['length'], flags=flow_entry['flags'], table_id=flow_entry['table_id'],
                                    idle_timeout=flow_entry['idle_timeout'], cookie=flow_entry['cookie'],
                                    packet_count=flow_entry['packet_count'], hard_timeout=flow_entry['hard_timeout'],
                                    byte_count=flow_entry['byte_count'], match=saved_match)
        flow.actions.set(actions)

    return Response(response)

@api_view(['GET'])
def get_switch_details(request, switch_id):
    ryu_controller_service = RyuControllerService()
    response = ryu_controller_service.get_switch_details(switch_id)
    return Response(response)


@swagger_auto_schema(methods=['post'], request_body=CreateFlowEntrySerializer)
@api_view(['POST'])
def add_flow_entry(request):
    if request.method == 'POST':
        serializer = CreateFlowEntrySerializer(data=request.data)
        if serializer.is_valid():
            if not Switch.objects.filter(dpid=serializer.validated_data['dpid'], connected=True).exists():
                return Response("Switch does not exist", status=404)
            ryu_controller_service = RyuControllerService()
            response = ryu_controller_service.add_flow_entry(serializer.validated_data)
            if response.status_code == 200:
                return Response("Flow entry added successfully", status=201)
            else:
                return Response("Error adding flow entry", status=500)
        return Response(serializer.errors)
    else:
        return Response("Invalid request method")



