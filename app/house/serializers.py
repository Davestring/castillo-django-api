"""House serializers module."""

from rest_framework import serializers

from ..address.serializers import AddressSerializer
from ..house.models import HouseModel
from ..service.serializers import ServiceSerializer
from ..wifi.serializers import WiFiSerializer


class HouseSerializer(serializers.ModelSerializer):
    """HouseSerializer.

    Extends from ModelSerializer and convert a queryset of the HouseModel
    class into a native python datatype.

    """

    address = AddressSerializer(read_only=False)

    services = ServiceSerializer(many=True, read_only=True)

    wifi = WiFiSerializer(many=True, read_only=True)

    class Meta:
        """Meta.

        Inner Meta class of HouseSerializer, it will allow to add custom
        rules to the serialized information.

        Attributes
        ----------
        fields : str
            Fields that should be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST request.

        """

        fields = (
            "id",
            "title",
            "description",
            "rating",
            "active",
            "address",
            "services",
            "wifi",
        )

        model = HouseModel

        read_only_fields = ("id", "created", "updated")
