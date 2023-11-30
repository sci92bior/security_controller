import json
import logging

import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from security_controller import settings
from security_controller.alert_collector.serializers import AlertSerializer
from security_controller.hpi.service import send_icmp_packet

logger = logging.getLogger(__name__)


@swagger_auto_schema(methods=['post'], request_body=AlertSerializer)
@api_view(['POST'])
def add_alert(request):
    if request.method == 'POST':
        logger.warning("Alert received")
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            alert = serializer.save()
            logger.warning("Checking if alert is associated with VIP service")
            if alert.is_associated_with_vip_service():
                # send alert to main resident with post request on 127.0.0.1:10000/alerts/
                logger.warning(f"Alert associated with VIP service. Sending alert to main resident. Detected attack "
                               f"type: {alert.alert_type} src ip: {alert.src_ip} dst ip: {alert.dst_ip}")
                headers = {
                    'accept': 'application/json',
                    'Content-Type': 'application/json',
                }
                requests.post(settings.MAIN_RESIDENT_URL + "/alerts/", headers=headers, data=json.dumps(serializer.data))
                #send_icmp_packet(settings.MAIN_RESIDENT_URL, json.dumps(serializer.data))
                logger.warning("Alert sent to main resident")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Invalid request method")