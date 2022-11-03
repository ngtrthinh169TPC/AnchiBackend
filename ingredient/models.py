from django.db import models


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"
