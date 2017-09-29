from __future__ import unicode_literals

from  accounts.models import *


class OrderItem(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    restaurant = models.ForeignKey(Restaurant)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    order_item = models.ManyToManyField(OrderItem, related_name="order_item")
    order_buyer = models.ForeignKey(User, related_name="order_buyer")
    order_waiter = models.ForeignKey(User, related_name="order_waiter")
    order_restaurant = models.ForeignKey(Restaurant, related_name="order_restaurant")
