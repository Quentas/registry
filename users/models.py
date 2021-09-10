from django.db import models
from django.db.models.deletion import DO_NOTHING
from allauth.socialaccount.models import SocialAccount 


class City(models.Model):
    first_layer = models.TextField(blank=False, max_length=10)
    second_layer = models.TextField(blank=False, max_length=10)
    third_layer = models.TextField(blank=False, max_length=10)
    fourth_layer = models.TextField(blank=False, max_length=10)
    category = models.CharField(blank=True, max_length=1)
    name = models.TextField(blank=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class UserData(models.Model):
    user = models.ForeignKey(SocialAccount, blank=False, on_delete=DO_NOTHING)
    city = models.ForeignKey(City, blank=False, on_delete=DO_NOTHING)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.extra_data['name'] + ' / ' + self.city.name + ' / Verified: ' + str(self.verified)
