from .models import Anime
from rest_framework import serializers

class AnimeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Anime
        fields = "__all__"