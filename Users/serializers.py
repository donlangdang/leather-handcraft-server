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
  # ở đây phải gọi hàm create_user nếu không thì password sẽ không được hash
  # nếu bên view data đã đc valid(.is_valid() và gọi .save()
  # mà không có hàm này thì raw data sẽ vô luôn mà ko đc hash(password)
  # gọi class GetAllUsers bên view thì data=request.data sẽ được đưa qua đây để xử lí
  # và gọi tới hàm này để create_user
  # nhớ tab vào để nó nằm trong class nha :)))
  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      email = validated_data['email'],
      username = validated_data['username'],
      password = validated_data['password']
    )
    return user
  
  def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get('password', instance.password)
    instance.username = validated_data.get('username', instance.username)
    instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.is_staff = validated_data.get('is_staff', instance.is_staff)
    instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
    instance.is_active = validated_data.get('is_active', instance.is_active)
    instance.is_admin = validated_data.get('is_admin', instance.is_admin)
    instance.save()
    return instance
