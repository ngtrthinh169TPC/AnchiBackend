from rest_framework import serializers

from area.serializers import AreaSerializer
from ingredient.serializers import IngredientSerializer
from tag.serializers import TagSerializer
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(read_only=True, many=True)
    areas = AreaSerializer(read_only=True, many=True)
    class Meta:
        model = Food
        fields = ['id', 'name', 'image', 'description', 'address', 'recipe', 'tags', 'ingredients', 'areas', 'verified']