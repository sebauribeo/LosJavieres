from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.administrator, name='administrator'),
    path('administrator/editUser/<int:pk>',views.editUser, name='edit_user'),
    path('administrator/deleteUser/<int:pk>',views.deleteUser, name='delete_user'),
    path('login/', views.login, name='login'),
    path('login/new-user', views.newUser, name='new-user'),
    #     VISTAS PRODUCTOS
    path('products/', views.Products, name='products'),
    path('products/addProduct', views.addProduct, name='add_product'),
    path('products/productDetail/<int:pk>',
         views.detailProduct, name='product_detail'),
    path('products/deleteProduct/<int:pk>',
         views.deleteProduct, name='delete_product'),
    path('products/editProduct/<int:pk>',
         views.editProduct, name='edit_product'),
    path('products/send/<int:pk>', views.addCartProducts, name='send'),
    #     VISTAS CARRITO
    path('cart/', views.cart, name='cart'),
    path('cart/deleteProduct/<int:pk>',
         views.deleteCartProduct, name='delete_cart_product'),
    path('cart/clearProduct/', views.cleanCart, name='clear'),
    path('cart/add/<int:pk>', views.addQuantityProduct, name='add_quantity'),
    path('cart/sub/<int:pk>', views.subQuantityProduct, name='sub_quantity'),
]
