"""Service urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..address.views import AddressList, AddressDetail

urlpatterns = [
    path("", AddressList.as_view(), name="address-list"),
    path("<int:pk>/", AddressDetail.as_view(), name="address-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
