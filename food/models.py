from django.db import models

from tag.models import Tag
from ingredient.models import Ingredient


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    recipe = models.CharField(max_length=4096)
    tags = models.ManyToManyField(Tag)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.food_name + " (" + str(self.food_id) + ")"