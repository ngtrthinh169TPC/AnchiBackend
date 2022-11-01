from django.contrib import admin

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',
                    'address', 'recipe', 'tag_list', 'ingredient_list')

    def tag_list(self, obj):
        return [tag for tag in obj.tags.all()]

    def ingredient_list(self, obj):
        return [ingredient for ingredient in obj.ingredients.all()]


admin.site.register(Food, FoodAdmin)
