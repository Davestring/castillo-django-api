"""Payment views module."""
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey

from app.booking.models import Booking
from utils.exceptions import BadRequest

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(["POST"])
@permission_classes([HasAPIKey])
def payment(request: Request) -> Response:
    """Create a charge to the guest's bank account."""
    amount = request.data.get("amount")

    token = request.data.get("token")

    booking = get_object_or_404(Booking, pk=request.data.get("booking_id"))

    if amount is None or token is None:
        raise BadRequest

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency=settings.STRIPE_CURRENCY,
            description=f"{booking.name} - {booking.check_in} to {booking.check_out} - amount: ${amount / 100}",
            source=token,
        )

        return Response(charge, status=status.HTTP_200_OK)
    except Exception as err:
        raise BadRequest(err) from err
