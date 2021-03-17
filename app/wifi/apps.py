"""WiFi apps module."""

from django.apps import AppConfig


class WifiConfig(AppConfig):
    """WifiConfig.

    Extends from AppConfig and configure the Wifi application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "wifi"
