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
    created : DateField
        Date when the network information was created.
    updated : DateField
        Date when the network information was updated.

    """

    name = models.CharField(max_length=64)

    password = models.CharField(max_length=64)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    house = models.ForeignKey(
        HouseModel, default=None, on_delete=models.CASCADE, related_name="wifi"
    )

    def __str__(self):
        """__str__.

        Object representation in string format.

        """
        return self.name

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

        db_table = "wifi"

        verbose_name = "WiFi"

        verbose_name_plural = "WiFi Networks"
