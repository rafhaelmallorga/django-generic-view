from rest_framework import serializers

from .models import Album, Band


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
