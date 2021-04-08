"""Gallery models module."""

from django.db import models

from ..house.models import HouseModel


class GalleryModel(models.Model):
    """GalleryModel.

    Extends the Model class from models package and defines the fields for a
    Gallery registry.

    Attributes
    ----------
    image : TextField
        Base64 string representation of an image.
    house : ForeignKey
        Relation between gallery and houses.
    created : DateField
        Date when the network information was created.
    updated : DateField
        Date when the network information was updated.

    """

    image = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    house = models.ForeignKey(
        HouseModel,
        default=None,
        on_delete=models.CASCADE,
        related_name="gallery",
    )

    class Meta:
        """Meta.

        Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.
        verbose_name : str
            Custom model name.
        verbose_name_plural : str
            Custom model plural name.

        """

        db_table = "gallery"

        verbose_name = "Property Gallery"

        verbose_name_plural = "Property Gallery"
