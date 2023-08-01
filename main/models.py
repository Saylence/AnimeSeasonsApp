from django.db import models

class anime_list(models.Model):
    name = models.CharField(max_length= 200)
    anime_href = models.CharField(max_length= 200)
    img_href = models.CharField(max_length= 200)
    season = models.CharField(max_length= 10)
    year = models.CharField(max_length= 10)
    genre = models.CharField(max_length= 200)
