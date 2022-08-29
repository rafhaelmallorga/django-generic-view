from rest_framework.views import APIView, Request, Response, status

from bands.serializers import AlbumSerializer, BandSerializer

from .common_view import PostCommonView


class BandView(PostCommonView):
    common_serializer = BandSerializer

    # def post(self, request: Request) -> Response:
    #     serializer = BandSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status.HTTP_201_CREATED)


class AlbumView(PostCommonView):
    common_serializer = AlbumSerializer

    # def post(self, request: Request) -> Response:
    #     serializer = AlbumSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status.HTTP_201_CREATED)
