"""Health views module."""

from rest_framework.response import Response
from rest_framework.views import APIView


class HealthAPIView(APIView):
    """HealthAPIView.

    Extends from APIView and retrieves the current status of the API.

    Methods
    -------
    get()
        It should retrieve an HTTP 200 status code with a dummy response for the user.

    """

    def get(self, request: Response) -> Response:
        """GET Request.

        It should retrieve an HTTP 200 status code with a dummy response for the user.

        Returns
        -------
        Response
            An HTTP success ``Response`` if the server is up and running.

        """
        return Response({"status": "Ok!"})
