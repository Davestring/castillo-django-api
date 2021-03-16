"""Address serializers module."""

from rest_framework.serializers import ModelSerializer

from ..address.models import AddressModel


class AddressSerializer(ModelSerializer):
    """AddressSerializer.

    Extends from ModelSerializer and convert a queryset of the AddressModel
    class into a native python datatype.

    """

    class Meta:
        """Meta.

        Inner Meta class of AddressSerializer, it will allow to add custom
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

        fields = "__all__"

        model = AddressModel

        read_only_fields = ["id", "createdAt", "updatedAt"]
