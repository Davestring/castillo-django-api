"""Insight views module."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..insight.models import InsightModel
from ..insight.serializers import InsightSerializer


class InsightList(ListAPIView):
    """InsightList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : InisightSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = InsightModel.objects.all()

    serializer_class = InsightSerializer


class InsightDetail(RetrieveAPIView):
    """InsightDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : InisightSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = InsightModel.objects.all()

    serializer_class = InsightSerializer
