"""Mailing builders module."""
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from app.booking.models import Booking, Guest
from app.mailing.utils.functools import get_user_fullname


def booking_summary_email_builder(guest_email: str) -> str:
    """Load and build the booking summary template.

    Parameters
    ----------
    guest_email : str
        Guest's email address that will help to find its latest reservation information.

    """
    guest = get_object_or_404(Guest, email=guest_email)

    booking = Booking.objects.filter(guest__email=guest_email).order_by("-check_in").first()

    context = {
        "guest": get_user_fullname(guest),
        "check_in": booking.check_in,
        "check_out": booking.check_out,
    }

    return render_to_string("pages/booking.html", context)
