"""Comment apps module."""

from django.apps import AppConfig


class CommentConfig(AppConfig):
    """CommentConfig.

    Extends from AppConfig and configure the Comment application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "comment"
