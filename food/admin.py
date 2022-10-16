from django.contrib import admin

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_id', 'foodName', 'description', 'address', 'recipe')


admin.site.register(Food, FoodAdmin)
