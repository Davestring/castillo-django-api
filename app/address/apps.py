"""Address apps module."""

from django.apps import AppConfig


class AddressConfig(AppConfig):
    """AddressConfig.

    Extends from AppConfig and configure the Address application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "address"
