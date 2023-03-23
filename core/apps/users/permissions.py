from rest_framework import permissions

class AnonPermission(permissions.BasePermission):
    edit_methods = ("CREATE")

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if all([not request.user,request.method in self.edit_methods]):
            return True
        return False

class PublicPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

class OwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_owner:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_owner)

class SuperuserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_superuser)
