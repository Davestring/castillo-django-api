"""Gallery apps module."""

from django.apps import AppConfig


class GalleryConfig(AppConfig):
    """GalleryConfig.

    Extends from AppConfig and configure the Gallery application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "gallery"
