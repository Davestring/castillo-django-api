"""User apps module."""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """Extends from `AppConfig` and configure the User application.

    Attributes
    ----------
    default_auto_field: str
        Model default primary key.
    name : str
        Application name.

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "app.user"
