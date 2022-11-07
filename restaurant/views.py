import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestaurantSerializer
from tag.models import Tag


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
        restaurants = Restaurant.objects.all();
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(status=200, data=serializer.data)


class FavouriteRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        favourite_restaurants = Restaurant.objects.filter(favourite_restaurant=request.user.id)
        serializer = RestaurantSerializer(favourite_restaurants, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurant': serializer.data})


class NextRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
          restaurant_list = Restaurant.objects.exclude(blacklist_restaurant=request.user.id)
        else:
          restaurant_list = Restaurant.objects.all()
        seed = random.randint(0, restaurant_list.__len__() - 1)
        serializer = RestaurantSerializer(restaurant_list[seed])
        return Response(status=200, data={'nextRestaurant': serializer.data})