"""House views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..house.models import HouseModel
from ..house.serializers import HouseSerializer


class HouseList(ListCreateAPIView):
    """HouseList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : BaseManager
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer


class HouseDetail(RetrieveUpdateDestroyAPIView):
    """HouseDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer
