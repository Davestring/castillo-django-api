"""Catalog apps module."""
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Extends from AppConfig and configure the Catalog application.

    Attributes
    ----------
    default_auto_field: str
        Model default primary key.
    name : str
        Application name.

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app.catalog"
