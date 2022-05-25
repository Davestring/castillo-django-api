"""Service models module."""
from django.db.models import CharField, TextField

from utils import BaseModel


class Service(BaseModel):
    """Extends the `BaseModel` class from `utils.models` package and defines the fields for a Service registry.

    Attributes
    ----------
    description : TextField
        Service description.
    name : CharField
        Service name.

    """

    name = CharField(max_length=128, unique=True)
    description = TextField(blank=True, default=None, null=True)

    class Meta:
        """Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.

        """

        db_table = "service"
