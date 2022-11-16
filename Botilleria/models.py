from django.db import models

class Product(models.Model):
    try:
        name = models.CharField(max_length=100)
        image = models.CharField(max_length=500)
        price = models.IntegerField()
        stock = models.IntegerField()
        details = models.CharField(max_length=500)
        brand = models.CharField(max_length=50)
        category = models.CharField(max_length=100)

        class Meta:
            ordering = ['id']

    except Exception as e:
        print('Modelo no creado: ', e)


# class User(models.Model):
#     try:
#         role = models.CharField(min_lenght = 50)
#         name = models.CharField(min_lenght = 50)
#         last_name = models.CharField(min_lenght = 50)
#         email = models.CharField(min_lenght = 100, unique = True)
#         password = models.CharField(min_lenght = 50)
#     except Exception as e:
#         print('Modelo no creado: ', e)


# class Sold_products(models.Model):
#     try:
#         product = models.CharField(min_lenght = 100)
#         price = models.IntegerField()
#         quantity = models.IntegerField()
#         user = models.CharField(min_lenght = 100)
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Purchased_products(models.Model):
#     try:
#         product = models.CharField(min_lenght = 100)
#         price = models.IntegerField()
#         quantity = models.IntegerField()
#         supplier = models.CharField(min_lenght = 100)
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Ticket_purchase(models.Model):
#     try:
#         product_id = models.IntegerField()
#         sold_products = models.IntegerField()
#         quantity = models.IntegerField()
#         price = models.IntegerField()
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Purchase_invoice(models.Model):
#     try:
#         product_id = models.IntegerField()
#         sold_products = models.IntegerField()
#         quantity = models.IntegerField()
#         price = models.IntegerField()
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Collaborators(models.Model):
#     try:
#         name = models.CharField(min_lenght = 100)
#         last_name = models.CharField(min_lenght = 100)
#         rut = models.IntegerField()
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Purchase_invoice(models.Model):
#     try:
#         purchase_product_id = models.IntegerField()
#         neto = models.IntegerField()
#         iva = models.IntegerField()
#         purchase_date = models.DateField()
#         pay_day = models.DateField()
#     except Exception as e:
#         print('Modelo no creado: ', e)