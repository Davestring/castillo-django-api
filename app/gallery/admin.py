"""Gallery admin module."""

from django.contrib import admin

from ..gallery.models import GalleryModel


class GalleryAdmin(admin.ModelAdmin):
    """GalleryAdmin.

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

    search_fields = ("id",)

    list_display = ("id", "house_id", "created", "updated")

    fieldsets = ((None, {"fields": ("image",)}),)


admin.site.register(GalleryModel, GalleryAdmin)
