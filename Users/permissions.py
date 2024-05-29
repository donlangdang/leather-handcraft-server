from rest_framework import permissions


class PermissionsUserId(permissions.BasePermission):
  def has_permission(self, request, view):
    user_id = view.kwargs.get('pk')
    
    return request.user.is_authenticated and request.user.id == int(user_id)