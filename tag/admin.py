from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'tag_name')


admin.site.register(Tag, TagAdmin)
