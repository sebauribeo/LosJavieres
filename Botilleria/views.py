from django.shortcuts import get_object_or_404, redirect, render
from Botilleria.forms import ProductForm
from Botilleria.models import Product

# Create your views here.
def home(request):
    return render(request, 'Botilleria/home.html')

def products(request):
    product = Product.objects.all()
    return render(request, 'Botilleria/products.html', {'all_product': product})

def cart(request):
    return render(request, 'Botilleria/cart.html')

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
            return redirect('administrator')
        return render(request, 'Products/deleteProduct.html', {'product': product})
    except Exception as e:
        print('Producto no eliminado ', e)
