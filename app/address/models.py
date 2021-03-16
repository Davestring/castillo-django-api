"""Address model module."""

from django.db import models


class AddressModel(models.Model):
    """AddressModel.

    Extends the Model class from models package and defines the fields for a
    Address registry.

    Attributes
    ----------
    street : CharField
        Street where the property is located.
    number : CharField
        Outdoor number of the property.
    zipCode : IntegerField
        Postal Code where the property is located.
    colony : CharField
        Colony where the property is located.
    municipality : CharField
        Municipality where the property is located.
    state : CharField
        State where the property is located.
    country : CharField
        Country where the property is located, default is `MX`.
    references : TextField
        Property references, it will help to locate the property more easier.
    createdAt : DateField
        Date when the registry was created.
    updatedAt : DateField
        Date when the registry was updated.

    """

    street = models.CharField(max_length=128)
    number = models.CharField(max_length=16)
    zipCode = models.IntegerField()
    colony = models.CharField(max_length=128)
    municipality = models.CharField(max_length=128)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=2, default="MX")
    references = models.TextField(blank=True)
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

        db_table = "address"
