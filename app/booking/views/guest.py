"""Guest views model."""
from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from app.booking.models import Guest
from app.booking.serializers import GuestSerializer
from utils import IsAuthenticatedOrReadCreateOnly


class GuestViewSet(ModelViewSet):
    """Concrete views for listing, creating, updating and deleting Guest registries."""

    filterset_fields = {
        "email": ["contains", "exact"],
        "is_active": ["exact"],
        "name": ["contains", "exact"],
        "phone": ["contains", "exact"],
    }
    ordering_fields = ("email", "id", "name", "phone")
    permission_classes = [HasAPIKey, IsAuthenticatedOrReadCreateOnly]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
