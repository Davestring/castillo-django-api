"""Insight apps module."""

from django.apps import AppConfig


class InsightConfig(AppConfig):
    """InsightConfig.

    Extends from AppConfig and configure the Insight application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "insight"
