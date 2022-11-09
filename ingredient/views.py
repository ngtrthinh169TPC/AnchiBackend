from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientAPI(APIView):
    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tag = serializer.save()
        return Response(status=201, data=serializer.data)


class AllIngredientsAPI(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.filter(verified=True)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(status=200, data=serializer.data)
