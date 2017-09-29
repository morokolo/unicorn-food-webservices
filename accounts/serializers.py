from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_type', 'image', 'cellphone')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'latlong')


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ('id', 'user_profile', 'restaurant')
