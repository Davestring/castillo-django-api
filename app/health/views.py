"""Health views module."""
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey


class HealthAPIView(APIView):
    """Extends from `APIView` and retrieves the current status of the API.

    Methods
    -------
    get()
        Retrieve an HTTP 200 status code with a dummy response for the user.

    """

    permission_classes = [HasAPIKey]

    def get(self, request: Response) -> Response:
        """Retrieve an HTTP 200 status code with a dummy response for the user.

        Returns
        -------
        Response
            An HTTP success `Response` if the server is up and running.

        """
        return Response({"status": "Ok!"})
