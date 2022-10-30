"""Mailing views module."""
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from app.mailing.utils import MailingEvents, MailingSubjects, booking_summary_email_builder
from utils import BadRequest


@api_view(["POST"])
@permission_classes([HasAPIKey])
def mailing(request: Request) -> Response:
    """Triggers an email when this endpoint is called."""
    booking_id = request.data.get("booking_id")

    event = request.data.get("event")

    if booking_id is None or event is None:
        raise BadRequest

    if event == MailingEvents["BOOKING_SUMMARY"].name:
        message, recipient = booking_summary_email_builder(booking_id)

    send_mail(MailingSubjects[event].value, message, settings.EMAIL_HOST_USER, [recipient], html_message=message)

    return Response(status=status.HTTP_204_NO_CONTENT)
