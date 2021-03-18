"""Service models module."""

from django.db import models

from ..house.models import HouseModel


class ServiceModel(models.Model):
    """ServiceModel.

    Extends the Model class from models package and defines the fields for a
    Service registry.

    Attributes
    ----------
    title : CharField
        Service title.
    description : TextField
        Service description.
    active : BooleanField
        True if the service is active, otherwise False.
    created : DateField
        Date when the service was created.
    updated : DateField
        Date when the services was updated.

    """

    title = models.CharField(max_length=128, unique=True)

    description = models.TextField(blank=True)

    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    houses = models.ManyToManyField(HouseModel, related_name="services")

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

        db_table = "service"

        verbose_name = "Service"

        verbose_name_plural = "Services"
