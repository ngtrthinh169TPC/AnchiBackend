from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'verified')


admin.site.register(Ingredient, IngredientAdmin)
