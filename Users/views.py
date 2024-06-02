from .models import (
  CustomUser,
)
from .serializers import (
  GetAllUsers
)
from .permissions import PermissionsUserId
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny



# Create your views here.
class UserRegisterAndGetUserById(APIView):
  
  
  # tùy chỉnh permissions với phương thức get hoặc post trong class base
  def get_permissions(self):
    if self.request.method in ['GET', 'PUT']:
      return [PermissionsUserId()]
    elif self.request.method == 'POST':
      return [AllowAny()]
    return super().get_permissions()
  
  # đăng kí người dùng mới
  def post(self, request):
    dataSerializers = GetAllUsers(data=request.data)
    if dataSerializers.is_valid():
      dataSerializers.save()
      return Response(dataSerializers.data, status=status.HTTP_201_CREATED)
    return Response(dataSerializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
  # lấy data người dùng theo permissions
  # những ai có access token mới xem đc cái này
  # đại khái như ai đăng nhập thì coi đc á
  def get(self, request, pk):
    try:
      modelUserById = CustomUser.objects.get(pk=pk)
    except:
      return Response({'mess': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    getUserById = GetAllUsers(modelUserById)
    if not getUserById:
      return Response(getUserById.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(getUserById.data, status=status.HTTP_200_OK)
    
  # cập nhật thông tin user    
  def put(self, request, pk):
    user = CustomUser.objects.get(pk=pk)
    # lấy object user với pk rồi gắn vô làm đối số với GetAllUser
    # để nó biết được gắn vô gàm update bên đó.
    # partial=True dùng cái này để có thể cập nhật 1 phần
    dataUpdateUser = GetAllUsers(user, data=request.data, partial=True)
    if dataUpdateUser.is_valid():
      dataUpdateUser.save()
      return Response(dataUpdateUser.data, status=status.HTTP_201_CREATED)
    return Response(dataUpdateUser.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class GetAllUserAPI(APIView):
  
  # tạm thời thì để ai cũng lấy đc api này nhưng sau này chỉ có quản trị viên mới xem đc.
  permission_classes = [AllowAny]
  
  def get(self, request):
    if request.method == 'GET':
      try:
        getUserModel = CustomUser.objects.all()
      except:
        return Response({'mess': 'we have no user here'}, status=status.HTTP_400_BAD_REQUEST)
      userSerializer = GetAllUsers(getUserModel, many=True)
      if not userSerializer:
        return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
      return Response(userSerializer.data, status=status.HTTP_200_OK)

