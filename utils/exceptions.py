"""HTTP exceptions module."""
from rest_framework import status
from rest_framework.exceptions import APIException


class BadRequest(APIException):
    """HTTP BAD REQUEST error."""

    default_code = "bad_request"
    default_detail = "Something is missing on request body."
    status_code = status.HTTP_400_BAD_REQUEST


class NotFound(APIException):
    """HTTP NOT FOUND error."""

    default_code = "not_found"
    default_detail = "Resource not found."
    status_code = status.HTTP_404_NOT_FOUND
