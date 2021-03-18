"""Service views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..service.models import ServiceModel
from ..service.serializers import ServiceSerializer


class ServiceList(ListCreateAPIView):
    """ServiceList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = ServiceModel.objects.all()

    serializer_class = ServiceSerializer


class ServiceDetail(RetrieveUpdateDestroyAPIView):
    """ServiceDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = ServiceModel.objects.all()

    serializer_class = ServiceSerializer
