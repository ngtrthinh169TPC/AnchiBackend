from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant_id', 'restaurantName',
                    'address', 'menu', 'note')


admin.site.register(Restaurant, RestaurantAdmin)
