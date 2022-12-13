from rest_framework import permissions


class IsConsultant(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.consultantprofile.id
        )