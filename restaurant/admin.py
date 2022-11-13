from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'address', 'menu', 'note', 'tag_list', 'area_list', 'verified')

    def tag_list(self, obj):
        return [tag for tag in obj.tags.all()]

    def area_list(self, obj):
        return [area for area in obj.areas.all()]


admin.site.register(Restaurant, RestaurantAdmin)
