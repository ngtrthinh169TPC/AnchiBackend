from django.contrib import admin

from django.contrib.auth.models import User
from .models import AnchiUser


class AnchiUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',
                    'favourite_food_list', 'blacklist_food_list', 'favourite_restaurant_list', 'blacklist_restaurant_list')

    def favourite_food_list(self, obj):
        return [food for food in obj.favourite_food.all()]

    def blacklist_food_list(self, obj):
        return [food for food in obj.blacklist_food.all()]

    def favourite_restaurant_list(self, obj):
        return [food for food in obj.favourite_restaurant.all()]

    def blacklist_restaurant_list(self, obj):
        return [food for food in obj.blacklist_restaurant.all()]


admin.site.register(AnchiUser, AnchiUserAdmin)
