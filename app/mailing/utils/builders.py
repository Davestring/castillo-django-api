"""Mailing builders module."""
from typing import Tuple, Union

from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from app.booking.models import Booking
from app.mailing.utils.functools import get_user_fullname


def booking_summary_email_builder(booking_id: Union[int, str]) -> Tuple[str, str]:
    """Load and build the booking summary template.

    Parameters
    ----------
    booking_id : Union[int, str]
        Booking unique identifier that will help to retrieve the guest and booking information.

    """
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        "guest": get_user_fullname(booking),
        "check_in": booking.check_in,
        "check_out": booking.check_out,
    }

    return render_to_string("pages/booking.html", context), booking.email
