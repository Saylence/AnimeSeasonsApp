from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anime_list", views.get_anime_list, name="anime_list"),
    path("anime_list_form", views.get_anime_season, name="anime_list_form")
]