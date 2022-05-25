"""Utility permissions module."""
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request


class IsAuthenticatedOrReadCreateOnly(BasePermission):
    """The request is authenticated as a user, or is a read-only request, or is a create request."""

    def has_permission(self, request: Request, view):
        """Validate if the user has permissions to perform this request.

        Returns
        -------
        bool
            True if the user has permission, otherwise false.

        """
        user = request.user
        return bool(request.method in SAFE_METHODS or (user and user.is_authenticated) or request.method == "POST")
