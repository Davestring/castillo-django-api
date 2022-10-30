"""Booking serializers module."""
from rest_framework.serializers import ModelSerializer

from app.booking.models import Booking


class BookingSerializer(ModelSerializer):
    """Extends from `ModelSerializer` and convert a queryset of the `Booking` model into a native Python datatype."""

    class Meta:
        """Inner Meta class of `BookingSerializer`, it will allow to add custom rules to the serialized data.

        Attributes
        ----------
        fields : str
            Fields that should be included in the serializer.
        model : Service
            Model from where the serializer will retrieve information.
        read_only_fields : Tuple
            Fields that will not be editable when admins make POST/PATCH request.

        """

        fields = "__all__"
        model = Booking
        read_only_fields = ("id", "created", "updated")
