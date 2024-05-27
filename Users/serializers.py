from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
  CustomUser,
)

class GetAllUsers(serializers.ModelSerializer):
  
  class Meta:
    model = CustomUser
    fields = ('__all__')
    extra_kwargs = { 'password': { 'write_only': True } }

# hàm này để tạo user mới 
def create(self, validated_data):
  user = CustomUser.objects.create_user(
    email = validated_data['email'],
    username = validated_data['username'],
    date_of_birth = validated_data['date_of_birth'],
    password = make_password(validated_data['password'])
  )
  return user
