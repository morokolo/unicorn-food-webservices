from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ('title',)

class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ('description', 'title', 'price',)
    

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
