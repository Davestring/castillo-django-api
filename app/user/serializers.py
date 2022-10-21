"""User serializers module."""
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework.serializers import ModelSerializer

from app.user.models import User


class UserSerializer(ModelSerializer):
    """Extends from `ModelSerializer` and convert a queryset of the `User` model into a native Python datatype."""

    class Meta:
        """Inner Meta class of `UserSerializer`, it will allow to add custom rules to the serialized data.

        Attributes
        ----------
        exclude : str
            Fields that should not be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST/PATCH request.

        """

        exclude = ("groups", "password", "user_permissions")
        model = User
        read_only_fields = ("id", "created", "updated")


class UserCreateSerializer(BaseUserCreateSerializer):
    """Extends from `UserCreateSerializer` and convert a queryset of the `User` model into a native Python datatype."""

    class Meta:
        """Inner Meta class of `UserCreateSerializer`, it will allow to add custom rules to the serialized data.

        Attributes
        ----------
        exclude : str
            Fields that should not be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST/PATCH request.

        """

        exclude = ("groups", "user_permissions")
        model = User
        read_only_fields = ("id", "created", "updated")
