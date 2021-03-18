"""Comment serializers module."""

from rest_framework.serializers import ModelSerializer

from ..comment.models import CommentModel


class CommentSerializer(ModelSerializer):
    """CommentSerializer.

    Extends from ModelSerializer and convert a queryset of the CommentModel
    class into a native python datatype.

    """

    class Meta:
        """Meta.

        Inner Meta class of CommentSerializer, it will allow to add custom
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

        model = CommentModel

        read_only_fields = ("id", "comment", "created", "updated")
