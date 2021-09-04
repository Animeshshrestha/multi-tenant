from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as VError
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from app.users.models import Posts, User


class UserRegistrationSerializer(serializers.Serializer):
    """
    Customer signup serializer.
    """

    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    @staticmethod
    def get_user(data):
        return User(email=data["email"])

    def validate(self, data):
        password = data["password1"]
        errors = {}
        try:
            validate_password(password, user=self.get_user(data))
        except VError as e:
            errors["password1"] = e.messages
        if password != data["password2"]:
            errors["password2"] = "password1 and password2 did not match."
        if errors:
            raise serializers.ValidationError(errors)
        return data

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                _("A user with that email already exists.")
            )
        return email

    @transaction.atomic
    def create(self, validated_data):
        user = self.get_user(validated_data)
        user.set_password(validated_data["password1"])
        user.save()
        return user


class PostModelSerializers(serializers.ModelSerializer):
    """
    Post Model Serializer
    """

    user_email_address = serializers.CharField(source="user.email", read_only=True)
    post_owner = serializers.SerializerMethodField("get_post_owner")

    class Meta:
        model = Posts
        fields = [
            "id",
            "user_email_address",
            "message_text",
            "created_at",
            "updated_at",
            "post_owner",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def __init__(self, *args, **kwargs):

        fields = kwargs.get("context", {}).get("fields")

        super().__init__(*args, **kwargs)

        if fields is not None:

            allowed = set(fields)
            for field in allowed:
                self.fields.pop(field)

    def get_post_owner(self, obj):
        """
        Serializer method that checks if the current post is associated
        to the current context user or not to ensure the post can be
        edited by the respective users only
        """
        return True if self.context["user"] == obj.user else False
