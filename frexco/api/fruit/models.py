from django.db import models
from api.region.models import Region


class Fruit(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
