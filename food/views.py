import json
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
            ingredient_list = json.loads(request.data.get('ingredients'))
        for ingredient_id in ingredient_list:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            if (ingredient is None):
                continue
            food.ingredients.add(ingredient)

        if (request.data.get('tags') is None):
            tag_list = []
        else:
            tag_list = json.loads(request.data.get('tags'))
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
        return Response(status=200, data={'username': request.user.username, 'favouriteFoods': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite foods listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            food_id = request.data.get('foodId')
            if food_id is None:
                return Response(status=400, data={"detail": "You must provide a food in order add to your favourite list"})
            food = Food.objects.get(id=food_id)
            user.favourite_food.add(food)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        except Food.DoesNotExist:
            return Response(status=404, data={"detail": "Provided food is not found at food_id " + str(food_id)})
        serializer = FoodSerializer(user.favourite_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteFoods': serializer.data})

    def patch(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite foods listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            new_foods_list = json.loads(request.data.get('favouriteFoods'))
            if new_foods_list is None:
                return Response(status=400, data={"detail": "You must provide a list to update your favourite foods"})
            foods = []
            for food_id in new_foods_list:
                try:
                    food = Food.objects.get(id=food_id)
                    foods.append(food)
                except Food.DoesNotExist:
                    return Response(status=404, data={"detail": "Provided food is not found at food_id " + str(food_id)})
            user.favourite_food.set(foods)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        serializer = FoodSerializer(user.favourite_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteFoods': serializer.data})


class BlacklistFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist foods."})
        blacklist_foods = Food.objects.filter(Q(verified=True) & Q(blacklist_food=request.user.id))
        serializer = FoodSerializer(blacklist_foods, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistFoods': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist foods."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            food_id = request.data.get('foodId')
            if food_id is None:
                return Response(status=400, data={"detail": "You must provide a food in order add to your blacklist"})
            food = Food.objects.get(id=food_id)
            user.blacklist_food.add(food)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        except Food.DoesNotExist:
            return Response(status=404, data={"detail": "Provided food is not found at food_id " + str(food_id)})
        serializer = FoodSerializer(user.blacklist_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistFoods': serializer.data})

    def patch(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your blacklist foods listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            new_foods_list = json.loads(request.data.get('blacklistFoods'))
            if new_foods_list is None:
                return Response(status=400, data={"detail": "You must provide a list to update your blacklist foods"})
            foods = []
            for food_id in new_foods_list:
                try:
                    food = Food.objects.get(id=food_id)
                    foods.append(food)
                except Food.DoesNotExist:
                    return Response(status=404, data={"detail": "Provided food is not found at food_id " + str(food_id)})
            user.blacklist_food.set(foods)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        serializer = FoodSerializer(user.blacklist_food, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistFoods': serializer.data})


class NextFoodAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            food_list = Food.objects.filter(Q(verified=True) & ~Q(blacklist_food=request.user.id))
        else:
            food_list = Food.objects.filter(verified=True)
        last_food = request.data.get('lastFood')
        if last_food is not None:
            food_list = food_list.exclude(id=last_food)
        if (food_list.__len__() == 0):
            return Response(status=204, data={"detail": "We don't have any foods left :( come again later or try add some foods for us."})
        seed = random.randint(0, food_list.__len__() - 1)
        serializer = FoodSerializer(food_list[seed])
        return Response(status=200, data={'nextFood': serializer.data})
