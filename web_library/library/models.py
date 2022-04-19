from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)

class Anime(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    studio = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(validators=[MinValueValidator(1917), max_value_current_year], blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comment_main = models.CharField(max_length=255, default="")
    comment_detailed = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title


        
