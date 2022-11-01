from rest_framework import serializers

from ingredient.serializers import IngredientSerializer
from tag.serializers import TagSerializer
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(read_only=True, many=True)
    class Meta:
        model = Food
        fields = ['id', 'name', 'description', 'address', 'recipe', 'tags', 'ingredients']