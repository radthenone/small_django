from rest_framework import permissions

class PublicCreate(permissions.BasePermission):
    edit_methods = ("CREATE")

    def has_object_permission(self, request, view, obj):
        if all([not request.user,request.method in self.edit_methods]):
            return True
        return False

class OwnerLogin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_owner:
            return True
        return False

class OnlySuperUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False