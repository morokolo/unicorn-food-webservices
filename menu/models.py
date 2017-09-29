from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)

class MenuItem(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name='menu_item')

    def __str__(self):
        return self.title
