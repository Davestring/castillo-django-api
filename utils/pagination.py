"""Utility pagination module."""
from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """Definition of the pagination result set for the GET endpoints.

    Attributes
    ----------
    max_page_size : int
        If set, this is a numeric value indicating the maximum allowable requested page size. This attribute is only
        valid if page_size_query_param is also set.
    page_size : int
        A numeric value indicating the page size.
    page_size_query_param : str
        If set, this is a string value indicating the name of a query parameter that allows the client to set the page
        size on a per-request basis.

    """

    max_page_size = settings.DEFAULT_MAX_PAGE_SIZE
    page_size = settings.DEFAULT_PAGE_SIZE
    page_size_query_param = "page_size"
