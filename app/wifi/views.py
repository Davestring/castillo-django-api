"""WiFi views module."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..wifi.models import WiFiModel
from ..wifi.serializers import WiFiSerializer


class WiFiList(ListAPIView):
    """WiFiList.

    Concrete views for listing a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = WiFiModel.objects.all()

    serializer_class = WiFiSerializer


class WiFiDetail(RetrieveAPIView):
    """WiFiDetail.

    Concrete views for retrieve a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = WiFiModel.objects.all()

    serializer_class = WiFiSerializer
