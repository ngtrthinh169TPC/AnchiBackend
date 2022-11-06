from django.contrib import admin

from .models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'address', 'menu', 'note', 'tag_list')

    def tag_list(self, obj):
        return [tag for tag in obj.tags.all()]


admin.site.register(Restaurant, RestaurantAdmin)
