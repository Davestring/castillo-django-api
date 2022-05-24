"""Mailing subjects module."""
from enum import Enum


class MailingSubjects(Enum):
    """Mailing subjects.

    Attributes
    ----------
    BOOKING_SUMMARY: str
        Subject for users that have created a reservation.

    """

    BOOKING_SUMMARY = "Gracias por reservar en Casa Castillo"
