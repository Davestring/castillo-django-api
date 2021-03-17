"""Address admin module."""

from django.contrib import admin

from ..address.models import AddressModel


class AddressAdmin(admin.ModelAdmin):
    """AddressAdmin.

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

    search_fields = ("id", "zipCode", "state", "municipality", "colony")

    list_display = (
        "id",
        "colony",
        "municipality",
        "zipCode",
        "state",
        "country",
        "created",
        "updated",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "street",
                    "number",
                    "zipCode",
                    "colony",
                    "municipality",
                    "state",
                    "country",
                    "references",
                )
            },
        ),
    )


admin.site.register(AddressModel, AddressAdmin)
