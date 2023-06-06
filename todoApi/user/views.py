from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from django.contrib.auth import get_user_model
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from django.contrib import admin
admin.autodiscover()

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



class UserListView(APIView):
    """
    List all user or create a new one
    """
    # , TokenHasReadWriteScope
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        if not request.user.is_authenticated:
            raise AuthenticationFailed("Authentication credentials were not provided.")
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
