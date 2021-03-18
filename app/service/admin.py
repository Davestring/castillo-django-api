"""Service admin module."""

from django.contrib import admin
from django.utils.translation import gettext as _

from ..house.models import HouseModel
from ..service.models import ServiceModel


class ServiceAdmin(admin.ModelAdmin):
    """ServiceAdmin.

    Defines the actions that will be show in Django Admin.

    Attributes
    ----------
    ordering : List
        Order filter.
    search_fields : Tuple
        Filter options.
    list_display : List
        Columns to be show in the admin.
    fieldsets : Tuple
        Controls the layout of admin “add” and “change” pages.

    """

    ordering = ("id", "title")

    search_fields = ("id", "title", "active")

    list_display = (
        "id",
        "title",
        "description",
        "active",
        "created",
        "updated",
    )

    fieldsets = (
        (None, {"fields": ("title",)}),
        (_("Service Description"), {"fields": ("description",)}),
        (_("Is service active?"), {"fields": ("active",)}),
    )
