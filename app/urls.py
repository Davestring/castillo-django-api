"""app URL Configuration."""

from typing import List

from django.urls import URLPattern, include, path

urlpatterns: List[URLPattern] = [
    path("", include("app.health.urls")),
    path("", include("app.auth.urls")),
]
