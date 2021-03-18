"""House urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..house.views import (
    HouseCommentsList,
    HouseDetail,
    HouseList,
    HouseServicesList,
    HouseWiFiList,
)

urlpatterns = [
    path("", HouseList.as_view(), name="house-list"),
    path("<int:pk>/", HouseDetail.as_view(), name="house-detail"),
    path(
        "<int:pk>/comments/",
        HouseCommentsList.as_view(),
        name="house-comments-list",
    ),
    path(
        "<int:pk>/services/",
        HouseServicesList.as_view(),
        name="house-services-list",
    ),
    path(
        "<int:pk>/networks/",
        HouseWiFiList.as_view(),
        name="house-networks-list",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
