"""Service models module."""

from django.db import models


class Service(models.Model):
    """Service.

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
    createdAt : DateField
        Date when the service was created.
    updatedAt : DateField
        Date when the services was updated.

    """

    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
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

        db_table = "service"
