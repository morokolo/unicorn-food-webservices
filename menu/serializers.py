from rest_framework import serializers
from .models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'description', 'restaurant', 'price',)

class MenuSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(read_only=True)
    class Meta:
        model = Menu
        fields = ('id', 'title', 'menu_items')
