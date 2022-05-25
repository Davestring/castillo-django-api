"""Payment urls module."""
from django.urls import path

from app.payment.views import payment

urlpatterns = [
    path("payment/", payment, name="payment"),
]
