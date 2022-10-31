from rest_framework import serializers

from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['food_id', 'food_name', 'description', 'address', 'recipe', 'tags', 'ingredients']