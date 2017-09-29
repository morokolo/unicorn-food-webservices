from rest_framework import serializers
from .models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'description', 'restaurant', 'price',)
