"""House models module."""

from django.db import models

from ..address.models import AddressModel


class HouseModel(models.Model):
    """HouseModel.

    Extends the Model class from models package and defines the fields for a
    House registry.

    Attributes
    ----------
    title : CharField
        House meta title, this field should be unique.
    description : CharField
        House meta description.
    cover : TextField
        House cover image in base64.
    rating : FloatField
        House rating, default value its 0.
    active : BooleanField
        True if the house is active, otherwise False.
    address : OneToManyField
        References the AddressModel and attach an address to the house.
    services : ManyToManyField
        Creates an intermediate table for houses and services.
    created : DateField
        Date when the service was created.
    updated : DateField
        Date when the services was updated.

    """

    title = models.CharField(max_length=128, unique=True)

    description = models.TextField()

    cover = models.TextField(default=None)

    rating = models.FloatField(default=0.0)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    address = models.OneToOneField(
        AddressModel, on_delete=models.CASCADE, related_name="address"
    )

    def __str__(self):
        """__str__.

        Object representation in string format.

        """
        return self.title

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

        db_table = "house"

        verbose_name = "House"

        verbose_name_plural = "Houses"
