"""WiFi serializers module."""

from rest_framework import serializers

from ..wifi.models import WiFiModel


class WiFiSerializer(serializers.ModelSerializer):
    """WiFiSerializer.

    Extends from ModelSerializer and convert a queryset of the WiFiSerializer
    class into a native python datatype.

    """

    class Meta:
        """Meta.

        Attributes
        ----------
        fields : str
            Fields that should be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST request.

        """

        fields = ("id", "name", "password", "active", "created", "updated")

        model = WiFiModel

        read_only_fields = ("id", "created", "updated")
