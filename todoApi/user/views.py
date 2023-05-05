from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from rest_framework import status

from django.contrib import admin
admin.autodiscover()

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



class UserListView(APIView):
    """
    List all user or create a new one
    """
    
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    
    def get(self, request, format=None):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
