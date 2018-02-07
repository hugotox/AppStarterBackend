from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class TestEndPoint(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id):
        return Response({
            "data": "Data ID: {}".format(id)
        })


class TestJSON(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({
            "message": "Hello World from the API"
        })
