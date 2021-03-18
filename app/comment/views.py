"""Comment views module."""

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ..comment.models import CommentModel
from ..comment.serializers import CommentSerializer


class CommentList(ListCreateAPIView):
    """CommentList.

    Concrete views for listing and creating a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = CommentModel.objects.all()

    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """CommentDetail.

    Concrete views for retrieve, update and delete a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = CommentModel.objects.all()

    serializer_class = CommentSerializer
