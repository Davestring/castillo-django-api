"""Booking models module."""
from django.db.models import CharField, DateField, EmailField

from utils import BaseModel


class Booking(BaseModel):
    """Extends the `BaseModel` class from `utils.models` package and defines the fields for a Booking registry.

    Attributes
    ----------
    check_in : DateField
        Date when the guest will arrive to the facilities.
    check_out : DateField
        Date when the guest will leave the facilities.
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

    check_in = DateField()
    check_out = DateField()
    name = CharField(max_length=150)
    first_surname = CharField(max_length=150)
    last_surname = CharField(blank=True, default=None, max_length=150, null=True)
    email = EmailField()
    phone = CharField(max_length=25)

    class Meta:
        """Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.

        """

        db_table = "booking"
