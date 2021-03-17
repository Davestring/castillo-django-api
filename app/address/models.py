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
    created : DateField
        Date when the registry was created.
    updated : DateField
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """__str__.

        Object representation in string format.

        """
        return (
            f"{self.street} {self.number} {self.colony}, {self.zipCode}"
            f"{self.municipality}, {self.state}"
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

        db_table = "address"

        verbose_name = "Address"

        verbose_name_plural = "Addresses"
