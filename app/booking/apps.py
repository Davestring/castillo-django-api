"""Booking apps module."""
from django.apps import AppConfig


class BookingConfig(AppConfig):
    """Extends from `AppConfig` and configure the Booking application.

    Attributes
    ----------
    default_auto_field: str
        Model default primary key.
    name : str
        Application name.

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app.booking"
