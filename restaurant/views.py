import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestaurantSerializer


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
        restaurant_list = Restaurant.objects.all()
        seed = random.randint(0, restaurant_list.__len__() - 1)
        serializer = RestaurantSerializer(restaurant_list[seed])
        return Response(status=200, data={'nextRestaurant': serializer.data})