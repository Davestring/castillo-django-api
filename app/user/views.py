"""User views module."""

from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework.decorators import action
from app.user.models import User
from utils import NotFound


class UserViewSet(BaseUserViewSet):
    """Concrete views for listing, creating, updating and deleting User registries."""

    filterset_fields = {
        "email": ["contains", "exact"],
        "name": ["contains", "exact"],
        "is_staff": ["exact"],
        "is_superuser": ["exact"],
        "is_active": ["exact"],
    }
    ordering_fields = ("id", "email", "name")
    queryset = User.objects.all()

    @action(["get"], detail=False)
    def me(self, request, *args, **kwargs):
        """ME endpoint.

        Retrieve current authenticated user registry.

        Returns
        -------
        Response
            An HTTP 200 success ``Response`` if the HTTP method is a GET, PUT or PATCH.

        """
        self.get_object = self.get_instance
        return self.retrieve(request, *args, **kwargs)

    def activation(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def resend_activation(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def set_password(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def reset_password(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def reset_password_confirm(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def set_username(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def reset_username(self):
        """Overwritten endpoint since is not used."""
        raise NotFound

    def reset_username_confirm(self):
        """Overwritten endpoint since is not used."""
        raise NotFound
