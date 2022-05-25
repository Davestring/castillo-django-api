"""Health urls module."""
from django.urls import path

from app.health.views import HealthAPIView

urlpatterns = [
    path("health", HealthAPIView.as_view(), name="health"),
]
