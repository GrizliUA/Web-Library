from .models import Anime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)


class AnimeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Anime
        fields = "__all__"