from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=255)


class Album(models.Model):
    name = models.CharField(max_length=255)

    band = models.ForeignKey(
        "bands.Band", on_delete=models.CASCADE, related_name="albums"
    )
