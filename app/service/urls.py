"""Service urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..service.views import ServiceDetail, ServiceList

urlpatterns = [
    path("", ServiceList.as_view(), name="service-list"),
    path("<int:pk>/", ServiceDetail.as_view(), name="service-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
