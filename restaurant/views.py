import json
import random
from django.db.models import Q
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
            tag_list = json.loads(request.data.get('tags'))
        for tag_id in tag_list:
            tag = Tag.objects.get(id=tag_id)
            if (tag is None):
                continue
            restaurant.tags.add(tag)
            
        return Response(status=201, data=serializer.data)



class AllRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            restaurants = Restaurant.objects.filter(Q(verified=True) & ~Q(blacklist_restaurant=request.user.id))
        else:
            restaurants = Restaurant.objects.filter(verified=True)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(status=200, data=serializer.data)


class FavouriteRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        favourite_restaurants = Restaurant.objects.filter(Q(verified=True) & Q(favourite_restaurant=request.user.id))
        serializer = RestaurantSerializer(favourite_restaurants, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurants': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            restaurant_id = request.data.get('restaurantId')
            if restaurant_id is None:
                return Response(status=400, data={"detail": "You must provide a restaurant in order add to your favourite list"})
            restaurant = Restaurant.objects.get(id=restaurant_id)
            user.favourite_restaurant.add(restaurant)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        except Restaurant.DoesNotExist:
            return Response(status=404, data={"detail": "Provided restaurant is not found at restaurant_id " + str(restaurant_id)})
        serializer = RestaurantSerializer(user.favourite_restaurant, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurants': serializer.data})

    def patch(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your favourite restaurants listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            new_restaurants_list = json.loads(request.data.get('favouriteRestaurants'))
            if new_restaurants_list is None:
                return Response(status=400, data={"detail": "You must provide a list to update your favourite restaurants"})
            restaurants = []
            for restaurant_id in new_restaurants_list:
                try:
                    restaurant = Restaurant.objects.get(id=restaurant_id)
                    restaurants.append(restaurant)
                except Restaurant.DoesNotExist:
                    return Response(status=404, data={"detail": "Provided restaurant is not found at restaurant_id " + str(restaurant_id)})
            user.favourite_restaurant.set(restaurants)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        serializer = RestaurantSerializer(user.favourite_restaurant, many=True)
        return Response(status=200, data={'username': request.user.username, 'favouriteRestaurants': serializer.data})


class BlacklistRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist restaurants."})
        blacklist_restaurants = Restaurant.objects.filter(Q(verified=True) & Q(blacklist_restaurant=request.user.id))
        serializer = RestaurantSerializer(blacklist_restaurants, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistRestaurants': serializer.data})

    def post(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to blacklist restaurants."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            restaurant_id = request.data.get('restaurantId')
            if restaurant_id is None:
                return Response(status=400, data={"detail": "You must provide a restaurant in order add to your blacklist"})
            restaurant = Restaurant.objects.get(id=restaurant_id)
            user.blacklist_restaurant.add(restaurant)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        except Restaurant.DoesNotExist:
            return Response(status=404, data={"detail": "Provided restaurant is not found at restaurant_id " + str(restaurant_id)})
        serializer = RestaurantSerializer(user.blacklist_restaurant, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistRestaurants': serializer.data})

    def patch(self, request):
        if (request.user.is_anonymous):
            return Response(status=401, data={'detail': "You must sign in to have your blacklist restaurants listed."})
        try:
            user = AnchiUser.objects.get(id=request.user.id)
            new_restaurants_list = json.loads(request.data.get('blacklistRestaurants'))
            if new_restaurants_list is None:
                return Response(status=400, data={"detail": "You must provide a list to update your blacklist restaurants"})
            restaurants = []
            for restaurant_id in new_restaurants_list:
                try:
                    restaurant = Restaurant.objects.get(id=restaurant_id)
                    restaurants.append(restaurant)
                except Restaurant.DoesNotExist:
                    return Response(status=404, data={"detail": "Provided restaurant is not found at restaurant_id " + str(restaurant_id)})
            user.blacklist_restaurant.set(restaurants)
        except AnchiUser.DoesNotExist:
            return Response(status=401, data={"detail": "Invalid user credentials."})
        serializer = RestaurantSerializer(user.blacklist_restaurant, many=True)
        return Response(status=200, data={'username': request.user.username, 'blacklistRestaurants': serializer.data})


class NextRestaurantAPI(APIView):
    def get(self, request):
        if (request.user.is_authenticated):
            restaurant_list = Restaurant.objects.filter(Q(verified=True) & ~Q(blacklist_restaurant=request.user.id))
        else:
            restaurant_list = Restaurant.objects.filter(verified=True)
        last_restaurant = request.data.get('lastRestaurant')
        if last_restaurant is not None:
            restaurant_list = restaurant_list.exclude(id=last_restaurant)
        if (restaurant_list.__len__() == 0):
            return Response(status=204, data={"detail": "We don't have any restaurants left :( come again later or try add some restaurants for us."})
        seed = random.randint(0, restaurant_list.__len__() - 1)
        serializer = RestaurantSerializer(restaurant_list[seed])
        return Response(status=200, data={'nextRestaurant': serializer.data})