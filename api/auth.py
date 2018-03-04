from django.contrib.auth import login, logout
from rest_framework.compat import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import UserSerializer


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"user": UserSerializer(user).data})
        else:
            return Response({'error': 'Invalid user/password.'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        logout(request)
        return Response()


class WhoAmI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"user": UserSerializer(request.user).data})
        else:
            return Response({"user": None})
