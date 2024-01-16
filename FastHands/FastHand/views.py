from django.shortcuts import render
from rest_framework import generics
from .models import Users
from .serializers import UsersSerializer


class UsersViewSet(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


# http://127.0.0.1:8000/?format=api