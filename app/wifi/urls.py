"""WiFi urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..wifi.views import WiFiList, WiFiDetail

urlpatterns = [
    path("", WiFiList.as_view(), name="wifi-list"),
    path("<int:pk>/", WiFiDetail.as_view(), name="wifi-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
