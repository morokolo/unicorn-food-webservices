from django.contrib import admin
from .models import *




class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ('restuarant',)


class MenuCategoryAdmin(admin.ModelAdmin):
    model = MenuCategory
    list_display = ('title', 'menu',)


class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_display = ('user_profile', 'restaurant')


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
