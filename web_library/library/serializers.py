import io

from .models import Anime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)


#class LibraryModel:
 #   def __init__(self, title, genre, year, rating):
 #       self.title = title
 #       self.genre = genre
 #       self.year = year
 #       self.rating = rating

class AnimeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=255)
    studio = serializers.CharField(max_length=255)
    year = serializers.IntegerField(validators=[MinValueValidator(1917), max_value_current_year])
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    comment_main = serializers.CharField(max_length=255, default="")
    comment_detailed = serializers.CharField(max_length=255, default="")


#def encode():
    #model = LibraryModel('Grand Blue', 'Comedy', 2018, 10.0)
    #model_sr = AnimeSerializer(model)
    #print(model_sr.data,type(model_sr), sep='\n')
    #json = JSONRenderer().render(model_sr.data)
    #print(json)



#def decode():
    #stream = io.BytesIO(b'{"title":"Grand Blue","genre":"Comedy","year":2018,"rating":"10.0"}')
    #data = JSONParser().parse(stream)
    #serializer = AnimeSerializer(data=data)
    #serializer.is_valid()
    #print(serializer.validated_data)