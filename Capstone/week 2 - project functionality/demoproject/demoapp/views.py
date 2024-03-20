from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):  # Use viewsets.ModelViewSet instead of serializers.ModelSerializer
    queryset = User.objects.all()
    serializer_class = UserSerializer
