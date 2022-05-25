"""Booking views model."""
from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from app.booking.models import Booking
from app.booking.serializers import BookingSerializer
from utils import IsAuthenticatedOrReadCreateOnly


class BookingViewSet(ModelViewSet):
    """Concrete views for listing, creating, updating and deleting Booking registries."""

    filterset_fields = {
        "check_in": ["exact", "gt", "lt"],
        "check_out": ["exact", "gt", "lt"],
        "guest": ["exact"],
        "is_active": ["exact"],
    }
    ordering_fields = ("check_in", "check_out", "id")
    permission_classes = [HasAPIKey, IsAuthenticatedOrReadCreateOnly]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
