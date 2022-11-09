import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestaurantSerializer
from tag.models import Tag
from user.models import AnchiUser


class RestaurantAPI(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.save()

        if (request.data.get('tags') is None):
            tag_list = []
        else:
            tag_list = request.data.get('tags')
        for tag_id in tag_list:
            tag = Tag.objects.get(id=tag_id)
            if (tag is None):
                continue
            restaurant.tags.add(tag)
            
        return Response(status=201, data=serializer.data)



class AllRestaurantAPI(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.filter(verified=True);
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(status=200, data=serializer.data)


class FavouriteRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        favourite_restaurants = Restaurant.objects.filter(verified=True).filter(favourite_restaurant=request.user.id)
        serializer = RestaurantSerializer(favourite_restaurants, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurant': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        user = AnchiUser.objects.get(id=request.user.id)
        restaurant_id = request.data.get('restaurantId')
        restaurant = Restaurant.objects.get(id=restaurant_id)
        user.favourite_restaurant.add(restaurant)
        serializer = RestaurantSerializer(user.favourite_restaurant, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurant': serializer.data})


class BlacklistRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist restaurants."})
        blacklist_restaurants = Restaurant.objects.filter(verified=True).filter(blacklist_restaurant=request.user.id)
        serializer = RestaurantSerializer(blacklist_restaurants, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistRestaurant': serializer.data})


class NextRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
          restaurant_list = Restaurant.objects.filter(verified=True).exclude(blacklist_restaurant=request.user.id)
        else:
          restaurant_list = Restaurant.objects.filter(verified=True)
        seed = random.randint(0, restaurant_list.__len__() - 1)
        serializer = RestaurantSerializer(restaurant_list[seed])
        return Response(status=200, data={'nextRestaurant': serializer.data})