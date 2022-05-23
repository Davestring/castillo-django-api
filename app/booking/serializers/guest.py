"""Guest serializers module."""
from rest_framework.serializers import ModelSerializer

from app.booking.models import Guest


class GuestSerializer(ModelSerializer):
    """Extends from `ModelSerializer` and convert a queryset of the `Guest` model into a native Python datatype."""

    class Meta:
        """Inner Meta class of `GuestSerializer`, it will allow to add custom rules to the serialized data.

        Attributes
        ----------
        exclude : str
            Fields that should be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST/PATCH request.

        """

        fields = "__all__"
        model = Guest
        read_only_fields = ("id", "created", "updated")
