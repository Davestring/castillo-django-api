"""Comment views module."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..comment.models import CommentModel
from ..comment.serializers import CommentSerializer


class CommentList(ListAPIView):
    """CommentList.

    Concrete views for listing a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = CommentModel.objects.all()

    serializer_class = CommentSerializer


class CommentDetail(RetrieveAPIView):
    """CommentDetail.

    Concrete views for retrieve a model instance.

    Attributes
    ----------
    queryset : QuerySet
        The queryset that should be used for returning objects from this view.
    serializer_class : AddressSerializer
        Used for validating, deserializing input and for serializing output.

    """

    queryset = CommentModel.objects.all()

    serializer_class = CommentSerializer
