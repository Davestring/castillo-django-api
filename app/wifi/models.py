"""WiFi models module."""

from django.db import models

from ..house.models import HouseModel


class WiFiModel(models.Model):
    """WiFiModel.

    Extends the Model class from models package and defines the fields for a
    WiFi registry.

    Attributes
    ----------
    name : CharField
        Name of the WiFi network.
    password : CharField
        Password of the WiFi network.
    active : BooleanField
        True if the wifi network is active, otherwise False.
    house : ForeignKey
        Relation between wifi and houses.
    createdAt : DateField
        Date when the network information was created.
    updatedAt : DateField
        Date when the network information was updated.

    """

    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    active = models.BooleanField(default=True)

    house = models.ForeignKey(
        HouseModel, on_delete=models.CASCADE, default=None
    )

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

        db_table = "wifi"
