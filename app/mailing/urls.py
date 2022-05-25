"""Mailing urls module."""
from django.urls import path

from app.mailing.views import mailing

urlpatterns = [
    path("mailing/", mailing, name="mailing"),
]
