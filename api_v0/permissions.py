from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return bool(request.user.is_staff or request.user.role == 'admin')

    def has_object_permission(self, request, view, obj):
        ij = request.method
        if request.method in ('PATCH', 'DELETE') and request.user.is_authenticated:
            return bool(obj.author == request.user or request.user.is_staff or request.user.role == 'admin')
        if request.user.is_authenticated:
            return True    
        if request.method in permissions.SAFE_METHODS:
            return True


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.is_staff or request.user.role == 'admin')


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return bool(request.user.is_staff or request.user.role == 'admin')
