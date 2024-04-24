from django.db import models

# Create your models here.
class CityName(models.Model):
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name
