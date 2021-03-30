"""Insight serializers module."""

from rest_framework import serializers

from ..insight.models import InsightModel


class InsightSerializer(serializers.ModelSerializer):
    """InsightSerializer.

    Extends from ModelSerializer and convert a queryset of the InsightModel
    class into a native python datatype.

    """

    class Meta:
        """Meta.

        Inner Meta class of InsightSerializer, it will allow to add custom
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

        model = InsightModel

        read_only_fields = ("id", "created", "updated")
