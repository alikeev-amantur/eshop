from rest_framework import permissions
from rest_framework.permissions import BasePermission

from users.models import NewUser


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsSupplier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        suppliers = NewUser.objects.filter(role=1)
        return user in suppliers
