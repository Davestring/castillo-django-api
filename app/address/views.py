"""Address views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..address.models import AddressModel
from ..address.serializers import AddressSerializer


class AddressList(ListCreateAPIView):
    """AddressList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = AddressModel.objects.all()

    serializer_class = AddressSerializer


class AddressDetail(RetrieveUpdateDestroyAPIView):
    """AddressDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = AddressModel.objects.all()

    serializer_class = AddressSerializer
