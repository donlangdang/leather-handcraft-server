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
class UserRegister(APIView):
  def post(self, request):
    dataSerializers = GetAllUsers(data=request.data)
    if dataSerializers.is_valid():
      dataSerializers.save()
      return Response(dataSerializers.data, status=status.HTTP_201_CREATED)
    return Response({'mess': 'khong thanh cong'}, status=status.HTTP_400_BAD_REQUEST)
