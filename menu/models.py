from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from accounts.models import Restaurant

# Create your models here.


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)

    def __str__(self):
        return self.restaurant.name


class MenuCategory(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    menu_category = models.ForeignKey(MenuCategory)
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.title






