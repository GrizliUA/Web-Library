from django.urls import path

from .views import *

urlpatterns = [
    path('anime/mine/', MyAnime.as_view()),
    path('anime/<int:pk>/', AnimeByID.as_view()),
    path('anime/genre/<slug:slug>/', AnimeByGenre.as_view()),
    path('anime/user/<int:pk>/', AnimeByUserID.as_view()),
    path('anime/', AnimeList.as_view()),
]