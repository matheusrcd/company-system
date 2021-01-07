from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=255)
    price = models.FloatField(default=None)
    category = models.TextField(max_length=255)

    def __str__(self):
        return self.name
