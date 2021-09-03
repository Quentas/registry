from django.db import models
from django.db.models.deletion import DO_NOTHING


class City(models.Model):
    first_layer = models.TextField(blank=False, max_length=10)
    second_layer = models.TextField(blank=False, max_length=10)
    third_layer = models.TextField(blank=False, max_length=10)
    fourth_layer = models.TextField(blank=False, max_length=10)
    categoty = models.CharField(blank=True, max_length=1)
    name = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'Cities'

class User(models.Model):
    name = models.TextField(max_length=100)
    city = models.ForeignKey(City, blank=True, on_delete=DO_NOTHING)
    verified = models.BooleanField(default=False)