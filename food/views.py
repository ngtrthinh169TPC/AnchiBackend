from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Food
from .serializers import FoodSerializer


class AllFoodAPI(APIView):
    def get(self, request):
        foods = Food.objects.all();
        serializer = FoodSerializer(foods, many=True)
        return Response(status=200, data=serializer.data)