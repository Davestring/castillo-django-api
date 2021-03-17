"""WiFi admin module."""

from django.contrib import admin
from django.utils.translation import gettext as _

from ..wifi.models import WiFiModel


class WiFiAdmin(admin.ModelAdmin):
    """WiFiAdmin.

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

    ordering = ("id",)

    search_fields = ("id", "name")

    list_display = ("id", "name", "active", "created", "updated")

    fieldsets = (
        (None, {"fields": ("name", "password")}),
        (_("Is WiFi network active?"), {"fields": ("active",)}),
    )


admin.site.register(WiFiModel, WiFiAdmin)
