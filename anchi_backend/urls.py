from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from user.views import UserAPI, LoginAPI, LogoutAPI
from food.views import FoodAPI, AllFoodAPI, FavouriteFoodAPI, BlacklistFoodAPI, NextFoodAPI
from ingredient.views import IngredientAPI, AllIngredientsAPI
from restaurant.views import RestaurantAPI, AllRestaurantAPI, FavouriteRestaurantAPI, BlacklistRestaurantAPI, NextRestaurantAPI
from tag.views import TagAPI, AllTagsAPI

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
    path('food/', FoodAPI.as_view(), name='food'),
    path('all-foods/', AllFoodAPI.as_view(), name='all-foods'),
    path('favourite-foods/', FavouriteFoodAPI.as_view(), name='favourite-foods'),
    path('blacklist-foods/', BlacklistFoodAPI.as_view(), name='blacklist-foods'),
    path('next-food/', NextFoodAPI.as_view(), name='next-food')
]

urlpatterns += [
    path('restaurant/', RestaurantAPI.as_view(), name='restaurant'),
    path('all-restaurants/', AllRestaurantAPI.as_view(), name='all-restaurants'),
    path('favourite-restaurants/', FavouriteRestaurantAPI.as_view(), name='favourite-restaurants'),
    path('blacklist-restaurants/', BlacklistRestaurantAPI.as_view(), name='blacklist-restaurants'),
    path('next-restaurant/', NextRestaurantAPI.as_view(), name='next-restaurant')
]

urlpatterns += [
    path('tag/', TagAPI.as_view(), name='tag'),
    path('all-tags/', AllTagsAPI.as_view(), name='all-tags')
]

urlpatterns += [
    path('ingredient/', IngredientAPI.as_view(), name='ingredient'),
    path('all-ingredients/', AllIngredientsAPI.as_view(), name='all-ingredients')
]