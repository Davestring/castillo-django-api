"""Booking models module."""
from django.db.models import DateField, ForeignKey, PROTECT

from utils import BaseModel


class Booking(BaseModel):
    """Extends the `BaseModel` class from `utils.models` package and defines the fields for a Booking registry.

    Attributes
    ----------
    check_in : DateField
        Date when the guests will arrive to the facilities.
    check_out : DateField
        Date when the guests will leave the facilities.
    guest : ForeignKey
        Guest related to this booking.

    """

    check_in = DateField()
    check_out = DateField()
    guest = ForeignKey("booking.guest", PROTECT, related_name="guests")

    class Meta:
        """Model meta options.

        Attributes
        ----------
        db_table : str
            The name of the database table to use for the model.

        """

        db_table = "booking"
