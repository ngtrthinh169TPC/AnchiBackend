from django.db import models


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    foodName = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    recipe = models.CharField(max_length=4096)
    # tag_list_id
    # ingredient_list_id

    def __str__(self):
        return self.foodName + " (" + str(self.food_id) + ")"
