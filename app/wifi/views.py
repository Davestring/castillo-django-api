"""WiFi views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..wifi.models import WiFiModel
from ..wifi.serializers import WiFiSerializer


class WiFiList(ListCreateAPIView):
    """WiFiList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : BaseManager
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = WiFiModel.objects.all()

    serializer_class = WiFiSerializer


class WiFiDetail(RetrieveUpdateDestroyAPIView):
    """WiFiDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = WiFiModel.objects.all()

    serializer_class = WiFiSerializer
