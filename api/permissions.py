from rest_framework import permissions
from .models.users import MyUser


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        x = [MyUser.RoleChoises.ADMIN.value, MyUser.RoleChoises.MODERATOR.value]
        return obj.author == request.user or request.user.role in x


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        x = [MyUser.RoleChoises.ADMIN.value]
        return request.user.is_staff or request.user.role in x


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        x = [MyUser.RoleChoises.ADMIN.value]
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.role in x)
