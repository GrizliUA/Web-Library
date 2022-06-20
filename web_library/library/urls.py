from django.urls import path

from .views import *

urlpatterns = [
    path('anime/mine/', MyAnimeAPI.as_view()),
    path('anime/<int:pk>/', AnimeAPIByID.as_view()),
    path('anime/genre/<slug:slug>/', AnimeAPIByGenre.as_view()),
    path('anime/user/<int:pk>/', AnimeAPIByUserID.as_view()),
    path('anime/', AnimeAPIList.as_view()),
]