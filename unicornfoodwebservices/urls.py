from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from accounts.views import *

router = routers.DefaultRouter()

router.register(r'userprofiles', UserProfileViewSet, base_name="user_profile")
router.register(r'restaurants', RestaurantViewSet, base_name='restaurants')
router.register(r'waiters', WaiterViewSet, base_name='waiters')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^epi/menu', include('menu.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
