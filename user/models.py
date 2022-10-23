from django.db import models

from django.contrib.auth.models import User
from food.models import Food
from restaurant.models import Restaurant


class AnchiUser(User):
    favourite_food = models.ManyToManyField(
        Food, related_name="favourite_food", blank=True)
    blacklist_food = models.ManyToManyField(
        Food, related_name="blacklist_food", blank=True)
    favourite_restaurant = models.ManyToManyField(
        Restaurant, related_name='favourite_restaurant', blank=True)
    blacklist_restaurant = models.ManyToManyField(
        Restaurant, related_name="blacklist_restaurant", blank=True)
