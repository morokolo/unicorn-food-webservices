from django.contrib import admin
from .models import *




class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ('restaurant', 'title', 'price')

admin.site.register(MenuItem, MenuItemAdmin)
