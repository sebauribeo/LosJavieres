from django.db import models

# Create your models here.
class Product(models.Model):
    try:
        name = models.CharField(max_length = 50)
        image = models.CharField(max_length = 500)
        price = models.IntegerField()
        stock = models.CharField(max_length = 32)
        details = models.CharField(max_length = 500)
        brand = models.CharField(max_length = 50)
    except Exception as e:
        print('Modelo no creado: ', e)
