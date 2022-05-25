"""Mailing events module."""
from enum import Enum


class MailingEvents(Enum):
    """Mailing events.

    Attributes
    ----------
    BOOKING_SUMMARY: str
        Event that notifies a guest the summary of its booking.

    """

    BOOKING_SUMMARY = "BOOKING_SUMMARY"
