from django.db import models

# Create your models here.


class Product(models.Model):
    try:
        name = models.CharField(max_length=50)
        image = models.CharField(max_length=500)
        price = models.IntegerField()
        stock = models.CharField(max_length=32)
        details = models.CharField(max_length=500)
        brand = models.CharField(max_length=50)
    except Exception as e:
        print('Modelo no creado: ', e)


# class User(models.Model):
#     try:
#         name = models.CharField(min_lenght = 50)
#         lastName = models.CharField(min_lenght = 50)
#         email = models.CharField(min_lenght = 100, unique = True)
#         password = models.CharField(min_lenght = 100)
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class promotionalProducts(models.Model):
#     try:
#         image = models.CharField(min_lenght = 500)
#         description = models.CharField(min_lenght = 500)
#         price = models.IntegerField()
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class ShoppingCart(models.Model):
#     try:
#         product = models.CharField(min_lenght = 100)
#         price = models.IntegerField()
#         quantity = models.IntegerField()
#         user = models.CharField(min_lenght = 100)
#     except Exception as e:
#         print('Modelo no creado: ', e)
