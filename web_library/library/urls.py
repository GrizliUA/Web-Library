from django.urls import path

from .views import *

urlpatterns = [
    path('anime/', AnimeAPIList.as_view()),
    path('anime/<int:pk>/', AnimeAPIUpdate.as_view()),
    path('animedelete/<int:pk>/', AnimeAPIDestroy.as_view()),
]