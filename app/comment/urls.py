"""Comment urls module."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..comment.views import CommentList, CommentDetail

urlpatterns = [
    path("", CommentList.as_view(), name="comment-list"),
    path("<int:pk>/", CommentDetail.as_view(), name="comment-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
