from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import BasicAuthentication

User = get_user_model()


class CustomAuthentication(BasicAuthentication):
    def authenticate_header(self, request):
        return 403


class AgencyAuthBackend(ModelBackend):
    """
    Backend for authenticating users with email and password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username or kwargs.get(User.USERNAME_FIELD)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
