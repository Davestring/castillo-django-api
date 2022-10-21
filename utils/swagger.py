"""Utility swagger module."""
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

SwaggerView = get_schema_view(
    openapi.Info(
        contact=openapi.Contact(email="davestringm@gmail.com"),
        default_version="v2.6.0",
        description=(
            "The panel below displays documentation of all endpoints, parameters and error messages available to the "
            "Casa Castillo API. If you have an API key, you can also test API calls directly from this panel."
        ),
        title="Casa Castillo API",
    ),
    public=True,
    permission_classes=(AllowAny,),
)
