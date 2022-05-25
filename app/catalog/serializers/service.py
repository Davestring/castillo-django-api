"""Service serializers module."""
from rest_framework.serializers import ModelSerializer

from app.catalog.models import Service


class ServiceSerializer(ModelSerializer):
    """Extends from `ModelSerializer` and convert a queryset of the `Service` model into a native Python datatype."""

    class Meta:
        """Inner Meta class of `ServiceSerializer`, it will allow to add custom rules to the serialized data.

        Attributes
        ----------
        exclude : str
            Fields that should be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST request.

        """

        fields = "__all__"
        model = Service
        read_only_fields = ("id", "created", "updated")
