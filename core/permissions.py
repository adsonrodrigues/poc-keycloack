from rest_framework import permissions


class IsAuthenticated(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super(IsAuthenticated, self).has_permission(request, view)
