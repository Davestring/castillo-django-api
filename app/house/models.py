"""House models module."""

from django.db import models

from ..address.models import AddressModel
from ..service.models import ServiceModel


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
    rating : FloatField
        House rating, default value its 0.
    active : BooleanField
        True if the house is active, otherwise False.
    address : OneToManyField
        References the AddressModel and attach an address to the house.
    services : ManyToManyField
        Creates an intermediate table for houses and services.
    createdAt : DateField
        Date when the service was created.
    updatedAt : DateField
        Date when the services was updated.

    """

    title = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    active = models.BooleanField(default=True)

    address = models.OneToOneField(AddressModel, on_delete=models.CASCADE)
    services = models.ManyToManyField(ServiceModel)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta.

        Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.

        """

        db_table = "house"
