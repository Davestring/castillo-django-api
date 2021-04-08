"""Gallery views module."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..gallery.models import GalleryModel
from ..gallery.serializers import GallerySerializer


class GalleryList(ListAPIView):
    """GalleryList."""

    queryset = GalleryModel.objects.all()

    serializer_class = GallerySerializer


class GalleryDetail(RetrieveAPIView):
    """GalleryList."""

    queryset = GalleryModel.objects.all()

    serializer_class = GallerySerializer
