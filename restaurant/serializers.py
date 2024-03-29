from rest_framework import serializers

from area.serializers import AreaSerializer
from tag.serializers import TagSerializer
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'image', 'description', 'address', 'menu', 'note', 'tags', 'areas', 'verified']
