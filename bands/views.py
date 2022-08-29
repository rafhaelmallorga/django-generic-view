from rest_framework.views import APIView, Request, Response, status

from bands.serializers import BandSerializer


class BandView(APIView):
    def post(self, request: Request) -> Response:
        serializer = BandSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
