from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Anime
from .permissions import ReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import AnimeSerializer


class MyAnime(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnimeSerializer

    def get_queryset(self):
        user = self.request.user
        return Anime.objects.filter(user=user)

class AnimeByID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    serializer_class = AnimeSerializer
    
    def get_queryset(self, **kwargs):
         pk = self.kwargs.get('pk')
         return Anime.objects.filter(id=pk)

class AnimeByGenre(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        return Anime.objects.filter(genre=slug)

class AnimeByUserID(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer

    def get_queryset(self, **kwargs):
        uid = self.kwargs.get('pk')
        return Anime.objects.filter(user=uid)

class AnimeList(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()
