"""Catalog urls module."""
from rest_framework.routers import DefaultRouter
from app.catalog.views import ServiceViewSet

router = DefaultRouter()

router.register("service", ServiceViewSet, basename="service")

urlpatterns = router.urls
