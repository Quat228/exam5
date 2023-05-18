from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user and request.user.is_authenticated and request.user.author:
                return True
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        try:
            if request.user and request.user.is_authenticated and request.user.author == obj.author:
                return True
        except Exception as e:
            return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user and request.user.is_authenticated and request.user.author:
                return True
        except Exception as e:
            return False
