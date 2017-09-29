from rest_framework import serializers
from .models import *
from menu.serializers import MenuSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'user_type', 'cellphone')


class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'latlong', 'menu')


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ('id', 'user_profile', 'restaurant')
