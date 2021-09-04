from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class ApiKeyPermission(BasePermission):
    """
    Custom Permission for checking request object
    has tenant attribute
    """

    def has_permission(self, request, view):
        if not request.tenant:
            raise PermissionDenied(detail="Api key was not provided.")
        return True


class UnauthenticatedPost(BasePermission):
    """
    Custom Permission for unauthenticated user
    and view action of type list
    """

    def has_permission(self, request, view):

        return request.method in ["GET"] and view.action in ["list"]
