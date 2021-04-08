"""Gallery urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..gallery.views import GalleryList, GalleryDetail

urlpatterns = [
    path("", GalleryList.as_view(), name="gallery-list"),
    path("<int:pk>/", GalleryDetail.as_view(), name="gallery-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
