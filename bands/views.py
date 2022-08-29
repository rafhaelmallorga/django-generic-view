from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from bands.serializers import AlbumSerializer, BandSerializer

from .common_view import GetCommonView, PostCommonView
from .models import Album, Band

# class BandView(PostCommonView, GetCommonView):
#     common_serializer = BandSerializer
#     common_model = Band


class BandView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = BandSerializer
    queryset = Band.objects.all()


class AlbumView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
