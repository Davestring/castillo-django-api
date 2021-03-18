"""House views module."""

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from ..comment.serializers import CommentSerializer
from ..house.models import HouseModel
from ..house.serializers import HouseSerializer
from ..service.serializers import ServiceSerializer
from ..wifi.serializers import WiFiSerializer


class HouseList(ListAPIView):
    """HouseList.

    Concrete views for listing a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer


class HouseDetail(RetrieveAPIView):
    """HouseDetail.

    Concrete views for retrieve a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer


class HouseCommentsList(ListAPIView):
    """HouseCommentsList.

    Concrete views for listing a House model instance and get the comments
    that belongs to that instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        """GET Request."""
        instance = self.get_object()
        comments = instance.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class HouseServicesList(ListAPIView):
    """HouseServicesList.

    Concrete views for listing a House model instance and get the services
    that belongs to that instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        """GET Request."""
        instance = self.get_object()
        services = instance.services.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class HouseWiFiList(ListAPIView):
    """HouseWiFiList.

    Concrete views for listing a House model instance and get the wifi networks
    that belong to that instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : HouseSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = HouseModel.objects.all()

    serializer_class = HouseSerializer

    def get(self, request, *args, **kwargs):
        """GET Request."""
        instance = self.get_object()
        networks = instance.wifi.all()
        serializer = WiFiSerializer(networks, many=True)
        return Response(serializer.data)
