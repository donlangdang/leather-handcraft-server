from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# django.contrib.auth.admin. UserAdmin là một lớp chuẩn của Django để quản lý người dùng trong giao diện quản trị. Lớp này cung cấp giao diện và các chức năng quản lý người dùng như thay đổi mật khẩu, tạo tài khoản mới, v.v.

admin.site.register(CustomUser, UserAdmin)