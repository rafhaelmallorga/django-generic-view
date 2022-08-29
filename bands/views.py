from rest_framework.views import APIView, Request, Response, status

from bands.serializers import AlbumSerializer, BandSerializer


class BandView(APIView):
    common_serializer = BandSerializer

    def post(self, request: Request) -> Response:
        serializer = BandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class AlbumView(APIView):
    common_serializer = AlbumSerializer

    def post(self, request: Request) -> Response:
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
