"""House admin module."""

from django.contrib import admin
from django.utils.translation import gettext as _

from ..gallery.models import GalleryModel
from ..house.models import HouseModel
from ..wifi.models import WiFiModel

# from ..service.models import ServiceModel


# class ServiceInline(admin.StackedInline):
#     """ServiceInline.

#     Edit the Service model in the House admin page.

#     Attributes
#     ----------
#     model : WiFiModel
#         The model which the inline is using.
#     extra : int
#         Number of extra forms to display in addition to the initial forms.
#     min_num : int
#         Minimum number of forms to show in the inline.

#     """

#     model = ServiceModel.houses.through

#     extra = 0

#     min_num = 1


class GalleryInline(admin.TabularInline):
    """GalleryInline.

    Edit the Gallery model in the House admin page.

    Attributes
    ----------
    model : GalleryModel
        The model which the inline is using.
    exclude : tuple
        Fields to exclude of editting of the child model.
    extra : int
        Number of extra forms to display in addition to the initial forms.
    min_num : int
        Minimum number of forms to show in the inline.
    max_num : int
        Maximum number of forms to show in the inline.

    """

    model = GalleryModel

    extra = 0

    min_num = 1

    max_num = 5


class WiFiInline(admin.TabularInline):
    """WiFiInline.

    Edit the WiFi model in the House admin page.

    Attributes
    ----------
    model : WiFiModel
        The model which the inline is using.
    exclude : tuple
        Fields to exclude of editting of the child model.
    extra : int
        Number of extra forms to display in addition to the initial forms.
    min_num : int
        Minimum number of forms to show in the inline.
    max_num : int
        Maximum number of forms to show in the inline.

    """

    model = WiFiModel

    exclude = ("active",)

    extra = 0

    min_num = 1

    max_num = 5


# @admin.register(ServiceModel)
class HouseAdmin(admin.ModelAdmin):
    """HouseAdmin.

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

    # inlines = (ServiceInline, WifiInline)
    inlines = (GalleryInline,)

    ordering = ("id",)

    search_fields = ("id", "title", "description", "active")

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
        (_("House Description"), {"fields": ("description",)}),
        (
            _("House Information"),
            {"fields": ("beds", "bathrooms", "rooms", "guests")},
        ),
        (_("House Price"), {"fields": ("price",)}),
        (_("House Address"), {"fields": ("address",)}),
        (_("Is house active?"), {"fields": ("active",)}),
    )


admin.site.register(HouseModel, HouseAdmin)
