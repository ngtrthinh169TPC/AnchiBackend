from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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
