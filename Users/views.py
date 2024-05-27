from django.shortcuts import render
from .models import (
  CustomUser,
)
from .serializers import (
  GetAllUsers
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


# Create your views here.
class UserRegister(generics.CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = GetAllUsers
  
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
