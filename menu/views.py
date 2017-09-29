from rest_framework.generics import RetrieveAPIView
from menu.models import MenuItem
from menu.serializers import MenuItemSerializer


class MenuItemsByRestaurantId(RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'restaurant'


