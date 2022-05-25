"""Booking urls module."""
from rest_framework.routers import DefaultRouter

from app.booking.views import BookingViewSet, GuestViewSet

router = DefaultRouter()

router.register("booking", BookingViewSet, basename="booking")
router.register("guest", GuestViewSet, basename="guest")

urlpatterns = router.urls
