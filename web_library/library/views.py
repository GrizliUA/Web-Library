from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Anime
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly 
from .serializers import AnimeSerializer


class AnimeAPIList(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class AnimeAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class AnimeAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = (IsAdminOrReadOnly, )