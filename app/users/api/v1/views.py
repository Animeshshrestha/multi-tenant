from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.api_key.permissions import UnauthenticatedPost
from app.core.pagination import DynamicPageSizePagination
from app.users.models import Posts

from .serializers import PostModelSerializers, UserRegistrationSerializer

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        "password1", "password2", "new_password1", "new_password2"
    )
)


class UserRegisterView(CreateAPIView):
    """
    Registers the user and creates the customer of that user
    and sends email for verification.

    Accepts the following POST parameters: username, email, mobile, first_name,
    last_name, password, password2
    """

    serializer_class = UserRegistrationSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(UserRegisterView, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"detail": _("User Created Successfully")},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class PostsViewSets(viewsets.ModelViewSet):
    """
    ViewSet that creates, displays, updates and delete
    the posts.
    Custom Pagination class with custom permission classes

    """

    queryset = Posts.objects.all().select_related("user")
    serializer_class = PostModelSerializers
    http_method_names = ["get", "options", "post", "delete", "patch"]
    permission_classes = [IsAuthenticated | UnauthenticatedPost]
    pagination_class = DynamicPageSizePagination

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        context = {}
        queryset = self.queryset.order_by("-created_at")
        page = self.paginate_queryset(queryset)
        # checking if authorization is present or not
        if request.headers.get("Authorization", None) is None:
            fields_to_exclude = ["post_owner"]
            context["fields"] = fields_to_exclude
        else:
            context["user"] = request.user
        if page is not None:
            serializer = self.serializer_class(
                queryset, many=True, read_only=True, context=context
            )
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(
            queryset, many=True, read_only=True, context=context
        )
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # checking if the posts  belong to request user or not
        if instance.user != request.user:
            raise PermissionDenied("Cannot Edit the Posts")
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # checking if the posts  belong to request user or not
        if instance.user != request.user:
            raise PermissionDenied("Cannot Delete the Posts")
        return super().destroy(request, *args, **kwargs)
