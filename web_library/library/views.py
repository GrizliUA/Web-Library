from unicodedata import category
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Anime
from .serializers import AnimeSerializer



class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    #queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Anime.objects.all()[:3]
        return Anime.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def genres(self, request, pk = None):
        anime = Anime.objects.get(pk=pk)
        return Response({'genres': anime.genre})











# class AnimeAPIList(generics.ListCreateAPIView): #GET/POST
#     queryset = Anime.objects.all()
#     serializer_class = AnimeSerializer



# class AnimeAPIUpdate(generics.UpdateAPIView):   #PUT
#     queryset = Anime.objects.all()
#     serializer_class = AnimeSerializer    




# class AnimeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):    #CRUD
#     queryset = Anime.objects.all()
#     serializer_class = AnimeSerializer  



#class AnimeAPIView(APIView):
    #def get(self, request):
        #anime = Anime.objects.all()
        #return Response({'posts': AnimeSerializer(anime,many=True).data})

    #def post(self,request):
        #serializer = AnimeSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        
        #return Response({'post': serializer.data})

    #def put(self, request, *args, **kwargs):
        #pk = kwargs.get("pk",None)
        #if not pk:
            #return Response({"error": "Method PUT not allowed"})
        
        #try:
            #instance = Anime.objects.get(pk=pk)
        #except:
            #return Response({"error": "Object PUT not exist"})

        #serializer = AnimeSerializer(data=request.data, instance=instance)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response({"post": serializer.data})

    #def delete(self, request, *args, **kwargs):
        #pk = kwargs.get("pk",None)
        #if not pk:
            #return Response({"error": "Method DELETE not allowed"})

        #try:
            #instance = Anime.objects.delete(pk=pk)
        #except:
            #return Response({"error": "Object DELETE not exist"})

        #serializer = AnimeSerializer(data=request.data, instance=instance)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()


        #return Response({"post": "delete post" + str(pk)})        