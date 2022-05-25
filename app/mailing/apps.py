"""Mailing apps module."""
from django.apps import AppConfig


class MailingConfig(AppConfig):
    """Extends from `AppConfig` and configure the Mailing application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "app.mailing"
