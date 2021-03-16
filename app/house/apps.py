"""House apps module."""

from django.apps import AppConfig


class HouseConfig(AppConfig):
    """HouseConfig.

    Extends from AppConfig and configure the House application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "house"
