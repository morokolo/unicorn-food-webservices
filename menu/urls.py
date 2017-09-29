from django.conf.urls import url

from menu import views

urlpatterns = [
    url(r'restaurant/(?P<restaurant>[0-9]+)/items$', views.MenuItemsByRestaurantId.as_view(), name='menu_items'),


