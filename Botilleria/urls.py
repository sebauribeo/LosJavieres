from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('administrator/', views.administrator, name='administrator'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('products/addProduct', views.addProduct, name='add_product'),
    path('products/productDetail/<int:pk>',
         views.detailProduct, name='product_detail'),
    path('products/deleteProduct/<int:pk>',
         views.deleteProduct, name='delete_product'),
    path('products/editProduct/<int:pk>',
         views.editProduct, name='edit_product'),
]
