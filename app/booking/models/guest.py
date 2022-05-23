"""Guest models module."""
from django.db.models import CharField, EmailField

from utils import BaseModel


class Guest(BaseModel):
    """Extends the `BaseModel` class from `utils.models` package and defines the fields for a Guest registry.

    Attributes
    ----------
    email : EmailField
        Guest's email.
    first_surname : CharField
        Guest's first surname.
    last_surname : CharField
        Guest's last surname.
    name : CharField
        Guest's name and middle name.
    phone : CharField
        Guest's phone number.

    """

    name = CharField(max_length=40)
    first_surname = CharField(max_length=25)
    last_surname = CharField(blank=True, default=None, max_length=25, null=True)
    email = EmailField(unique=True)
    phone = CharField(max_length=12)

    class Meta:
        """Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.

        """

        db_table = "guest"
