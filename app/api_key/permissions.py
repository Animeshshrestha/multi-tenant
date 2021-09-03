from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class ApiKeyPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.tenant:
            raise PermissionDenied(detail='Api key was not provided.')
        return True

class UnauthenticatedPost(BasePermission):
    def has_permission(self, request, view):

        return request.method in ['GET'] and view.action in ['list']
