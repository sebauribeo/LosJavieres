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


class User(models.Model):
    try:
        name = models.CharField(max_length = 50)
        last_name = models.CharField(max_length = 50)
        email = models.CharField(max_length = 100, unique = True)
        password = models.CharField(max_length = 50)
        class Meta:
            ordering = ['id']

    except Exception as e:
        print('Modelo no creado: ', e)



# class Purchased_products(models.Model):
#     try:
#         user_id = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
#         product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
#         price = models.IntegerField()
#         quantity = models.IntegerField()
#         supplier = models.CharField(max_length = 100)
#         date = models.DateField()
        
#         class Meta:
#             ordering = ['id']
        
#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Ticket_purchase(models.Model):
#     try:
#         product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
#         purchase_product_id = models.ForeignKey(Purchased_products, on_delete=models.CASCADE, null = True)

#         class Meta:
#             ordering = ['id']

#     except Exception as e:
#         print('Modelo no creado: ', e)

# class Purchase_invoice(models.Model):
#     try:
#         product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
#         purchase_product_id = models.ForeignKey(Purchased_products, on_delete=models.CASCADE, null = True)

#         class Meta:
#             ordering = ['id']

#     except Exception as e:
#         print('Modelo no creado: ', e)


