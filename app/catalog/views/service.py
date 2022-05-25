"""Service views model."""
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from app.catalog.models import Service
from app.catalog.serializers import ServiceSerializer


class ServiceViewSet(ModelViewSet):
    """Concrete views for listing, creating, updating and deleting Service registries."""

    filterset_fields = {"is_active": ["exact"], "name": ["contains", "exact"]}
    ordering_fields = ("id", "name")
    permission_classes = [HasAPIKey, DjangoModelPermissionsOrAnonReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
