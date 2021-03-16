"""Service apps module."""

from django.apps import AppConfig


class ServiceConfig(AppConfig):
    """ServiceConfig.

    Extends from AppConfig and configure the Service application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "service"
