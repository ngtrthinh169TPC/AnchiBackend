from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from user.views import UserAPI, LoginAPI, LogoutAPI
from food.views import AllFoodAPI, FavouriteFoodAPI, NextFoodAPI
from restaurant.views import AllRestaurantAPI, FavouriteRestaurantAPI, NextRestaurantAPI

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.DefaultRouter()
router.register(r'user', UserAPI)

urlpatterns += [
    url('', include(router.urls)),
    path('login/', LoginAPI.as_view(), name='user-login'),
    path('logout/', LogoutAPI.as_view(), name='user-logout')
]

urlpatterns += [
    path('all-foods/', AllFoodAPI.as_view(), name='all-foods'),
    path('favourite-foods/', FavouriteFoodAPI.as_view(), name='favourite-foods'),
    path('next-food/', NextFoodAPI.as_view(), name='next-food')
]

urlpatterns += [
    path('all-restaurants/', AllRestaurantAPI.as_view(), name='all-restaurants'),
    path('favourite-restaurants/', FavouriteRestaurantAPI.as_view(), name='favourite-restaurants'),
    path('next-restaurant/', NextRestaurantAPI.as_view(), name='next-restaurant')
]