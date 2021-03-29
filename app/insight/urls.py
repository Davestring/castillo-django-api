"""Insight urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..insight.views import InsightList, InsightDetail

urlpatterns = (
    path("", InsightList.as_view(), name="insight-list"),
    path("<int:pk>/", InsightDetail.as_view(), name="Insight-detail"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
