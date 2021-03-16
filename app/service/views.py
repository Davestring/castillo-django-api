"""Service views module."""

from typing import Optional

from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from utils.responses import CustomResponse

from ..service.models import ServiceModel
from ..service.serializers import ServiceSerializer


class ServiceList(views.APIView):
    """ServiceList.

    Wrapper that retrieves all the resources from the Service table.

    Methods
    -------
    get(request)
        Retrieves all the resources information of the Service table.
    post(request)
        Creates a new registry for the Service table.

    """

    def get(self, request: Request) -> Response:
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
        queryset = ServiceModel.objects.all()

        services = ServiceSerializer(queryset, many=True).data

        return CustomResponse(
            data=services,
            message="Services information as been successfully retrieved.",
        ).success()

    def post(self, request: Request) -> Response:
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
        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return CustomResponse(
                data=serializer.data, message="Registry successfully created."
            ).success()

        return CustomResponse(
            data=serializer.errors, message="Something went wrong!"
        ).error()


class ServiceDetail(views.APIView):
    """ServiceDetail.

    Wrapper that allows to perform CRUD operations to a single Service element.

    Methods
    -------
    _get_resource(primary_key)
        Search for a single register in the table using the PK.
    get(request, primary_key)
        Retrieves the detailed information of a Service resource.
    put(request, primary_key)
        Updates a single registry of the Service table.
    delete(request, primary_key)
        Deletes a single registry of the Service table.

    """

    @classmethod
    def _get_queryset(cls, primary_key: int) -> Optional[ServiceModel]:
        """Get Resource.

        Search for a single register in the table using the PK.

        Parameters
        ----------
        primary_key : int
            Resource primary key.

        Returns
        -------
        Service if the PK exists, otherwise None.

        """
        try:
            return ServiceModel.objects.get(pk=primary_key)
        except ServiceModel.DoesNotExist:
            return None

    def get(self, request: Request, primary_key: int) -> Response:
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
        queryset = self._get_queryset(primary_key)

        if not queryset:
            return CustomResponse(
                message="The resource does not exists."
            ).error(404)

        service = ServiceSerializer(queryset).data

        return CustomResponse(
            data=service,
            message="Information has been successfully retrieved.",
        ).success()

    def put(self, request: Request, primary_key: int) -> Response:
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
        queryset = self._get_queryset(primary_key)

        if not queryset:
            return CustomResponse(
                message="The resource does not exists."
            ).error(404)

        serializer = ServiceSerializer(queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return CustomResponse(
                data=serializer.data, message="Registry successfully updated."
            ).success()

        return CustomResponse(
            data=serializer.errors, message="Something went wrong!"
        ).error()

    def delete(self, request: Request, primary_key: int) -> Response:
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
        queryset = self._get_queryset(primary_key)

        if not queryset:
            return CustomResponse(
                message="The resource does not exists."
            ).error(404)

        queryset.delete()

        return CustomResponse(
            message="Registry successfully deleted."
        ).success()
