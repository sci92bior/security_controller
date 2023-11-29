import json

import requests
from rest_framework import serializers
from rest_framework.response import Response

from security_controller import settings
from security_controller.command_pusher.serializers import CreateFlowEntrySerializer

CONTROLLER_URL = settings.NETWORK_CONTROLLER_URL


class RyuControllerService:

    def get_switch_details(self, switch_id):
        # create a GET request to the controller
        # get the response
        # return the response
        response = requests.get(CONTROLLER_URL + "/stats/desc/" + str(switch_id))
        json_results = json.loads(response.content)[f'{switch_id}']
        return json_results

    def get_connected_switches(self):
        # create a GET request to the controller
        # get the response
        # return the response
        response = requests.get(CONTROLLER_URL + "/stats/switches")
        return json.loads(response.content)

    def get_flow_stats(self, switch_id):
        # create a GET request to the controller
        # get the response
        # return the response
        response = requests.get(CONTROLLER_URL + "/stats/flow/" + str(switch_id))
        json_results = json.loads(response.content)[f'{switch_id}']
        return json_results

    def add_flow_entry(self, data):
        # create a POST request to the controller
        # get the response
        # return the response
        response = requests.post(CONTROLLER_URL + "/stats/flowentry/add", json=data)

        return response

    def modify_flow_entry(self, data):
        # create a POST request to the controller
        # get the response
        # return the response
        response = requests.post(CONTROLLER_URL + "/stats/flowentry/modify", json=data)

        return response

    def delete_flow_entry(self, data):
        # create a POST request to the controller
        # get the response
        # return the response
        response = requests.post(CONTROLLER_URL + "/stats/flowentry/delete", json=data)

        return response

    def clear_all_flow_entries(self, dpid):
        # create a POST request to the controller
        # get the response
        # return the response
        response = requests.delete(CONTROLLER_URL + "/stats/flowentry/clear/"+dpid)

        return response

    def add_flow_entry_raw(self, data):
        serializer = CreateFlowEntrySerializer(data=data)
        if serializer.is_valid():

            response = self.add_flow_entry(serializer.validated_data)
            if response.status_code == 200:
                return True
            else:
                return False






