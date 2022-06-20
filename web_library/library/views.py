from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Anime
from .permissions import ReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import AnimeSerializer


class AnimeAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class MyAnimeAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnimeSerializer

    def get_queryset(self):
        user = self.request.user
        return Anime.objects.filter(user=user)

class AnimeAPIByID(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    serializer_class = AnimeSerializer
    
    def get_queryset(self, **kwargs):
         pk = self.kwargs.get('pk')
         return Anime.objects.filter(id=pk)

class AnimeAPIByGenre(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        return Anime.objects.filter(genre=slug)

class AnimeAPIByUserID(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer

    def get_queryset(self, **kwargs):
        uid = self.kwargs.get('pk')
        return Anime.objects.filter(user=uid)

class AnimeAPIList(generics.ListAPIView):
    permission_classes = [ReadOnly]
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()
    pagination_class = AnimeAPIListPagination
