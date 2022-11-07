from rest_framework import serializers

from tag.serializers import TagSerializer
from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'image', 'address', 'menu', 'note', 'tags', 'verified']
