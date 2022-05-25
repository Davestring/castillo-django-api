"""Utility models module."""
from django.db.models import BooleanField, DateTimeField, Model


class BaseModel(Model):
    """Application abstract base model.

    Extends the `Model` class from `django.db.models` package and defines the fields for a Base Model registry.
    This model will not be used to create any database table. Instead, when it is used as a base class for other
    models, its fields will be added to those of the child class.

    Attributes
    ----------
    created : DateTimeField
        Date when the registry was created.
    is_active : BooleanField
        True if the BaseModel is active, otherwise False.
    updated : DateTimeField
        Date when the BaseModel was updated.

    """

    is_active = BooleanField(default=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        """Model meta options.

        Attributes
        ----------
        abstract : bool
            Defines this model as an abstract class.

        """

        abstract = True
