from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"
