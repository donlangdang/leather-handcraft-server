from django.urls import path
from .views import (
    UserRegisterAndGetUserById,
    GetAllUserAPI
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('register/<int:pk>/', UserRegisterAndGetUserById.as_view()),
    path('register/', UserRegisterAndGetUserById.as_view()),
    path('updateuser/<int:pk>/', UserRegisterAndGetUserById.as_view()),
    path('getalluser/', GetAllUserAPI.as_view()),
    path('logintoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
]