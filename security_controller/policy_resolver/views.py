from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from security_controller.policy_resolver.serializer import PolicySerializer


@swagger_auto_schema(methods=['post'], request_body=PolicySerializer)
@api_view(['POST'])
def add_policy(request):
    if request.method == 'POST':
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Invalid request method")
