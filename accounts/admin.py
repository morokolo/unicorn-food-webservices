from django.contrib import admin
from .models import *

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latlong')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'cellphone')


class WaiterAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'restaurant')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Waiter, WaiterAdmin)
