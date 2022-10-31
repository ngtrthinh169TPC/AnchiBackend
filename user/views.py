from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from .serializers import UserSerializer


class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=request.data.get(
            'username'), password=request.data.get('password'))
        token = Token.objects.create(user=user)
        
        return Response(status=201, data={'username': user.username, 'token': token.key})

class LoginAPI(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(status=200, data={'username': user.username, 'token': token.key})
        return Response(status=400, data={'detail': 'Invalid user credentials.'})

class LogoutAPI(APIView):
    def post(self, request):
        print("dang")
        logout(request)
        print("at least we've logged out")
        return Response(status=200, data={'detail': 'Log out successfully.'})