from rest_framework.generics import RetrieveAPIView
from menu.models import MenuItem
from menu.serializers import MenuItemSerializer
from rest_framework.response import Response
import simplejson
from django.core import serializers
from django.http import HttpResponse
from rest_framework import status

class MenuItemsByRestaurantId(RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'restaurant'

    def get(self, request, *args, **kwargs):
        restaurant_id = kwargs.get('restaurant', None)
        if restaurant_id:
            menu_items = MenuItem.objects.filter(restaurant=restaurant_id)
            json_data = serializers.serialize('json', menu_items)

            return HttpResponse(serializers.serialize('json', menu_items), content_type="application/json")
            #return Response(json_data, status=status.HTTP_200_OK)
        errors = {
            'error': ['No restaurant was selected']
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
