from rest_framework import serializers
from .models import *
from accounts.serializers import *

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('title', 'description', 'restaurant', 'price')

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemsSerializer(read_only=True)
    buyer = User(read_only=True)

    class Meta:
        model = Order
        fields = ('item', 'order_buyer', 'order_waiter', 'order_restaurant')
