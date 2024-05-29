from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

"""
  BaseUserManager là một class mặc định được cung cấp bởi Django framework để quản lý việc tạo và xác thực người dùng (user authentication).
  Nó cung cấp các phương thức cần thiết để thực hiện các tác vụ cơ bản như tạo người dùng, xác thực đăng nhập, kiểm tra quyền truy cập, v.v.
  - Phải làm BaseUserManager để có thể dùng các phương thức create_user và có thể tạo dduocj superuser
  - Nói chung là phải làm cái này mới dùng được như bình thường cái này như kiểu custom lại các fiedl trong user và superuser...
  - quản lí việc tạo user và superuser và các thao tác liên quan tới nó
  
"""
class CustomUserManager(BaseUserManager):
  
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('Email must be set')
    # hàm này normalize_email() dùng để chuẩn hóa email, đảm bảo tính nhất quán
    email = self.normalize_email(email)
    # Tạo một đối tượng người dùng mới bằng cách sử dụng mô hình người dùng (self.model),
    # truyền vào địa chỉ email và bất kỳ trường bổ sung nào thông qua **extra_fields
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)
    
    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True')
    return self.create_user(email, password, **extra_fields)
  
  
# tạo custom user mới  
class CustomUser(AbstractUser):
  username = models.CharField(max_length=150, null=True, unique=True)
  email = models.EmailField(max_length=150, unique=True)
  date_of_birth = models.DateField(null=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  
  # trường này dùng để tạo user và superuser và các thao tác liên quan tới user
  objects = CustomUserManager()
  
  # ở đây trường USERNAME_FIELD và EMAIL_FIELD dùng để authentication
  # có thể đăng nhập bằng email hoặc username
  # REQUIRED_FIELDS là không thể thiếu trong đăng kí người dùng
  USERNAME_FIELD = 'username'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['email']
  
  def __str__(self):
    return self.email
  
