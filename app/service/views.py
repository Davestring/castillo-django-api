"""Service views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.request import Request
from rest_framework.response import Response

from ..service.models import ServiceModel
from ..service.serializers import ServiceSerializer


class ServiceList(ListCreateAPIView):
    """ServiceList.

    Wrapper that retrieves all the resources from the Service table.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        The serializer class that should be used for validating and
        deserializing input, and for serializing output.

    Methods
    -------
    get(request)
        Retrieves all the resources information of the Service table.
    post(request)
        Creates a new registry for the Service table.

    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """GET Request.

        Retrieves all the resources information of the Service table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """POST Request.

        Creates a new registry for the Service table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.create(request, *args, **kwargs)


class ServiceDetail(RetrieveUpdateDestroyAPIView):
    """ServiceDetail.

    Wrapper that allows to perform CRUD operations to a single Service element.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        The serializer class that should be used for validating and
        deserializing input, and for serializing output.

    Methods
    -------
    get(request, primary_key)
        Retrieves the detailed information of a Service resource.
    put(request, primary_key)
        Updates a single registry of the Service table.
    delete(request, primary_key)
        Deletes a single registry of the Service table.

    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """GET Request.

        Retrieves the detailed information of a Service resource.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.
        primary_key : int
            Resource primary key.

        Returns
        -------
        Response

        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """PUT Request.

        Updates a single registry of the Service table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.
        primary_key : int
            Resource primary key.

        Returns
        -------
        Response

        """
        return self.update(request, *args, **kwargs)

    def delete(
        self, request: Request, *args: tuple, **kwargs: dict
    ) -> Response:
        """DELETE Request.

        Deletes a single registry of the Service table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.
        primary_key : int
            Resource primary key.

        Returns
        -------
        Response

        """
        return self.destroy(request, *args, **kwargs)
