from django.db import models

from area.models import Area
from tag.models import Tag
from ingredient.models import Ingredient


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(upload_to='images/foods', default='')
    description = models.CharField(max_length=1024, blank=True)
    address = models.CharField(max_length=1024, blank=True)
    recipe = models.CharField(max_length=4096, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    areas = models.ManyToManyField(Area, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"
