"""Comment admin module."""

from django.contrib import admin
from django.utils.translation import gettext as _

from ..comment.models import CommentModel


class CommentAdmin(admin.ModelAdmin):
    """CommentAdmin.

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

    ordering = ("id", "name")

    search_fields = ("id", "name", "lastname", "active")

    list_display = (
        "id",
        "name",
        "lastname",
        "comment",
        "active",
        "created",
        "updated",
    )

    fieldsets = (
        (None, {"fields": ("comment",)}),
        (_("User name and lastname"), {"fields": ("name", "lastname")}),
        (_("Is comment active?"), {"fields": ("active",)}),
    )


admin.site.register(CommentModel, CommentAdmin)
