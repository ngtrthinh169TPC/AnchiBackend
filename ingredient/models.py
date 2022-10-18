from django.db import models


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=256)

    def __str__(self):
        return self.ingredient_name + " (" + str(self.ingredient_id) + ")"
