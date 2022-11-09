from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ingredient
from .serializers import IngredientSerializer

class AllIngredientsAPI(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.filter(verified=True)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(status=200, data=serializer.data)
