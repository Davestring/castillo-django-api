"""Mailing functools module."""
from typing import Union

from app.booking.models import Booking
from app.user.models import User


def get_user_fullname(user: Union[Booking, User]) -> str:
    """Obtain the user's fullname if it has, otherwise its email.

    Parameters
    ----------
    user : Union[Booking, User]
        Given user model to get its data.

    Returns
    -------
    str

    """
    if user.name is None or user.first_surname is None:
        return user.email
    if user.last_surname is None:
        return f"{user.name} {user.first_surname}"
    return f"{user.name} {user.first_surname} {user.last_surname}"
