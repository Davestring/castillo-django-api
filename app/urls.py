"""Application urls Configuration."""
from typing import List

from django.urls import URLPattern, include, path

from utils import SwaggerView

urlpatterns: List[URLPattern] = [
    path("", include("app.auth.urls")),
    path("", include("app.booking.urls")),
    path("", include("app.catalog.urls")),
    path("", include("app.health.urls")),
    path("docs/", SwaggerView.with_ui("redoc", cache_timeout=0), name="docs"),
]
