from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions

from user.models import CustomUser


class IsSupport(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Support":
            return True
        
    def has_object_permission(self, request, view, obj):
        return self.has_permission

class IsSales(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Vente":
            return True
        
    def has_object_permission(self, request, view, obj):
        return self.has_permission
        
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.role == "Gestion":
            return True
        
    def has_object_permission(self, request, view, obj):
        return self.has_permission