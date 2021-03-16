"""Address views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.request import Request
from rest_framework.response import Response

from ..address.models import AddressModel
from ..address.serializers import AddressSerializer


class AddressList(ListCreateAPIView):
    """AddressList.

    Concrete views for listing and creating a Address model instance.

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
        Retrieves all the resources information of the Address table.
    post(request)
        Creates a new registry for the Address table.

    """

    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """GET Request.

        Retrieves all the resources information of the Address table.

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

        Creates a new registry for the Address table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.create(request, *args, **kwargs)


class AddressDetail(RetrieveUpdateDestroyAPIView):
    """AddressDetail.

    Concrete views for retrieve, update and delete an Address model instance.

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
        Retrieves the detailed info of a single instance of the Address model.
    put(request, primary_key)
        Updates a single instance of the Address model.
    delete(request, primary_key)
        Deletes a single instance of the Address model.

    """

    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer

    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """GET Request.

        Retrieves the detailed info of a single instance of the Address model.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """PUT Request.

        Updates a single instance of the Address model.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.update(request, *args, **kwargs)

    def delete(
        self, request: Request, *args: tuple, **kwargs: dict
    ) -> Response:
        """DELETE Request.

        Deletes a single instance of the Address model.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        return self.destroy(request, *args, **kwargs)
