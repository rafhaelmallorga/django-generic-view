from django.urls import path

from . import views

urlpatterns = [
    path("bands/", views.BandView.as_view()),
    path("albums/", views.AlbumView.as_view()),
]
