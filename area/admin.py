from django.contrib import admin

from .models import Area


class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'verified')


admin.site.register(Area, AreaAdmin)
