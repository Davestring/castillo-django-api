"""Auth views module."""
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class AuthTokenView(TokenObtainPairView):
    """Takes a set of user credentials and returns an access and refresh JSON web token pair."""

    permission_classes = [HasAPIKey]


class AuthTokenRefreshView(TokenRefreshView):
    """Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid."""

    permission_classes = [HasAPIKey]
