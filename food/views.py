import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Food
from .serializers import FoodSerializer


class FoodAPI(APIView):
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201, data=serializer.data)


class AllFoodAPI(APIView):
    def get(self, request):
        foods = Food.objects.all();
        serializer = FoodSerializer(foods, many=True)
        return Response(status=200, data=serializer.data)


class FavouriteFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite foods listed."})
        favourite_foods = Food.objects.filter(favourite_food=request.user.id)
        serializer = FoodSerializer(favourite_foods, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteFood': serializer.data})


class NextFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
          food_list = Food.objects.exclude(blacklist_food=request.user.id)
        else:
          food_list = Food.objects.all()
        seed = random.randint(0, food_list.__len__() - 1)
        serializer = FoodSerializer(food_list[seed])
        return Response(status=200, data={'nextFood': serializer.data})
