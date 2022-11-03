from django.db import models

from tag.models import Tag


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024, blank=True)
    menu = models.CharField(max_length=4096, blank=True)
    note = models.CharField(max_length=1024, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"
