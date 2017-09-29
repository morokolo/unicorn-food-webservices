from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    latlong = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    USER_TYPE_CHOICES = (
        ('restaurant', 'Restaurant'),
        ('waiter', 'Waiter'),
        ('buyer', 'Buyer')
    )
    user = models.ForeignKey(User, related_name='user_profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='Media', height_field=None, width_field=None, max_length=100)
    cellphone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Waiter(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='waiter_user_profile')
    restaurant = models.OneToOneField(Restaurant, related_name='waiter_restaurant')


class BuyerHistory(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='buyer_history_restaurant')
    buyer = models.ForeignKey(UserProfile, related_name='buyer_history')
