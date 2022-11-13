import random
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Food
from .serializers import FoodSerializer
from ingredient.models import Ingredient
from tag.models import Tag
from user.models import AnchiUser


class FoodAPI(APIView):
    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        food = serializer.save()

        if (request.data.get('ingredients') is None):
            ingredient_list = []
        else:
            ingredient_list = request.data.get('ingredients')
        for ingredient_id in ingredient_list:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            if (ingredient is None):
                continue
            food.ingredients.add(ingredient)

        if (request.data.get('tags') is None):
            tag_list = []
        else:
            tag_list = request.data.get('tags')
        for tag_id in tag_list:
            tag = Tag.objects.get(id=tag_id)
            if (tag is None):
                continue
            food.tags.add(tag)
            
        return Response(status=201, data=serializer.data)


class AllFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            foods = Food.objects.filter(Q(verified=True) & ~Q(blacklist_food=request.user.id))
        else:
            foods = Food.objects.filter(verified=True)
        serializer = FoodSerializer(foods, many=True)
        return Response(status=200, data=serializer.data)


class FavouriteFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite foods listed."})
        favourite_foods = Food.objects.filter(Q(verified=True) & Q(favourite_food=request.user.id))
        serializer = FoodSerializer(favourite_foods, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteFood': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite foods listed."})
        user = AnchiUser.objects.get(id=request.user.id)
        food_id = request.data.get('foodId')
        food = Food.objects.get(id=food_id)
        user.favourite_food.add(food)
        serializer = FoodSerializer(user.favourite_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteFood': serializer.data})


class BlacklistFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist foods."})
        blacklist_foods = Food.objects.filter(Q(verified=True) & Q(blacklist_food=request.user.id))
        serializer = FoodSerializer(blacklist_foods, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistFood': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist foods."})
        user = AnchiUser.objects.get(id=request.user.id)
        food_id = request.data.get('foodId')
        food = Food.objects.get(id=food_id)
        user.blacklist_food.add(food)
        serializer = FoodSerializer(user.blacklist_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistFood': serializer.data})


class NextFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            food_list = Food.objects.filter(Q(verified=True) & ~Q(blacklist_food=request.user.id))
        else:
            food_list = Food.objects.filter(verified=True)
        if (food_list.__len__() == 0):
            return Response(status=204, data={"detail": "We don't have any foods left :( come again later or try add some foods for us."})
        seed = random.randint(0, food_list.__len__() - 1)
        serializer = FoodSerializer(food_list[seed])
        return Response(status=200, data={'nextFood': serializer.data})
