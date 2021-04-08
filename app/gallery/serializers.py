"""Gallery serializers module."""

from rest_framework import serializers

from ..gallery.models import GalleryModel


class GallerySerializer(serializers.ModelSerializer):
    """GallerySerializer.

    Extends from ModelSerializer and convert a queryset of the GalleryModel
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

        fields = ("id", "image", "created", "updated")

        model = GalleryModel

        read_only_fields = ("id", "created", "updated")
