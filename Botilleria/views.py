from django.shortcuts import get_object_or_404, redirect, render
from Botilleria.cart import Cart
from Botilleria.forms import ProductForm
from Botilleria.models import CartProducts, Product
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'Botilleria/home.html')

def products(request):
    product = Product.objects.all()
    return render(request, 'Botilleria/products.html', {'all_product': product})

def cart(request):
    product = Product.objects.all()
    return render(request, 'Botilleria/cart.html', {'all_product': product})

def login(request):
    return render(request, 'Botilleria/login.html')

def administrator(request):
    product = Product.objects.all()
    return render(request, 'Botilleria/admin.html', {'all_product': product})

# CRUD PRODUCTS

def addProduct(request):
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit = False)
                product.save()
                messages.success(request, 'Producto agregado...')
                return redirect('administrator')
        else:
            form = ProductForm()
        return render(request, 'Products/addProduct.html', {'form': form})
    except Exception as e:
        print('Producto no agregado ', e)

def detailProduct(request, pk):
    try:
        product = get_object_or_404(Product, pk = pk)
        return render(request, 'Products/productDetail.html', {'product': product})
    except Exception as e:
        print('El producto seleccionado no se actualizo', e)


def editProduct(request, pk):
    try:
        product = get_object_or_404(Product, pk = pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance = product)
            if form.is_valid():
                product = form.save(commit = False)
                product.save()
                messages.success(request, 'Producto modificado')
                return redirect('administrator')
        else:
            form = ProductForm(instance = product)
        return render(request, 'Products/editProduct.html', {'form': form})
    except Exception as e:
        print('producto no editado', e)

def deleteProduct(request, pk):
    try:
        product = get_object_or_404(Product, pk = pk)
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Producto eliminado')
            return redirect('administrator')
        return render(request, 'Products/deleteProduct.html', {'product': product})
    except Exception as e:
        print('Producto no eliminado ', e)


def addCartProducts(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id = pk)
        cart.addProduct(product)
        messages.success(request, 'Producto agregado al carro de compras')
        return redirect('products')
    except Exception as e:
        print('No se pudo agregar producto al carrito', e)

def deleteCartProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id = pk)
        cart.deleteCartProduct(product)
        messages.success(request, 'Producto eliminado del carro de compras')
        return redirect('cart')
    except Exception as e:
        print('No se pudo eliminar el producto', e)
        
def addQuantityProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id = pk)
        cart.addQuantityCartProduct(product)
        return redirect('cart')
    except Exception as e:
        print('No se pudo aumentar la cantidad', e)
        
def subQuantityProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id = pk)
        cart.subQuantityCartProduct(product)
        return redirect('cart')
    except Exception as e:
        print('No se pudo disminuir la cantidad', e)

def cleanCart(request):
    try:
        cart = Cart(request)
        cart.clearAllProducts()
        messages.success(request, 'Carro de compras limpio')
        return redirect('cart')
    except Exception as e:
        print('No se pudo limpiar el carrito', e)