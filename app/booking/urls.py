"""Booking urls module."""
from rest_framework.routers import DefaultRouter

from app.booking.views import GuestViewSet

router = DefaultRouter()

router.register("guest", GuestViewSet, basename="guest")

urlpatterns = router.urls
