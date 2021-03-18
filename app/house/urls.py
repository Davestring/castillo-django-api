"""House urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..house.views import HouseList, HouseDetail

urlpatterns = [
    path("", HouseList.as_view(), name="house-list"),
    path("<int:pk>/", HouseDetail.as_view(), name="house-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
