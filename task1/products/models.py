from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.IntegerField()
    availability = models.CharField(max_length=100)

    def __str__(self):
        return self.name
