"""Auth urls module."""
from django.urls import re_path

from app.auth.views import AuthTokenRefreshView, AuthTokenView

urlpatterns = [
    re_path(r"^jwt/create/?", AuthTokenView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", AuthTokenRefreshView.as_view(), name="jwt-refresh"),
]
