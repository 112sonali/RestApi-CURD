from django.shortcuts import render
from rest_framework import generics
from.models import *
from.serializers import UserSerializer

# Create your views here.

class userapi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class userview(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class listapi(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class deletedata(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

