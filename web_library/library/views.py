from genericpath import exists
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Anime
from .serializers import AnimeSerializer


class AnimeAPIView(APIView):
    def get(self, request):
        anime = Anime.objects.all()
        return Response({'posts': AnimeSerializer(anime,many=True).data})

    def post(self,request):
        serializer = AnimeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_new = Anime.objects.create(
            title=request.data['title'],
            genre=request.data['genre'],
            studio=request.data['studio'],
            year=request.data['year'],
            rating=request.data['rating'],
            comment_main=request.data['comment_main'],
            comment_detailed=request.data['comment_detailed']
        )
        return Response({'post': AnimeSerializer(post_new).data})