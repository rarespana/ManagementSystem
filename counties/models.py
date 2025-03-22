from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=25, default='None')
    state = models.CharField(max_length=25, default='activ')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class County(models.Model):
    admins = models.ManyToManyField(User)
    county_name = models.CharField(max_length=25)

    def __str__(self):
        return self.county_name
