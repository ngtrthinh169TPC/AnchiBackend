from django.db import models


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurantName = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    menu = models.CharField(max_length=4096)
    note = models.CharField(max_length=1024)
    # tag_list_id

    def __str__(self):
        return self.restaurantName + " (" + str(self.restaurant_id) + ")"
