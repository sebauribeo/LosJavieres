from django.shortcuts import get_object_or_404, redirect, render
from Botilleria.cart import Cart
from Botilleria.forms import LogInForm, ProductForm, UserAdminForm, UserForm
from Botilleria.models import Product, Purchased_products, Ticket_purchase
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import uuid


def home(request):
    product = Product.objects.filter(category='Promo')
    return render(request, 'Botilleria/home.html', {'promo': product})


def cart(request):
    product = Product.objects.all()
    return render(request, 'Botilleria/cart.html', {'all_product': product})


def signOut(request):
    messages.success(request, 'Haz terminado tu sesion...')
    logout(request)
    return redirect('home')


def logIn(request):
    try:
        if request.method == 'POST':
            form = LogInForm(request.POST)
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'Botilleria/login.html', {'form': form, 'error': 'Usuario o Contraseña Incorrectos'})
            else:
                login(request, user)
                messages.success(request, 'Sesion iniciada...')
                return redirect('home')
        else:
            form = LogInForm()
        return render(request, 'Botilleria/login.html', {'form': form})
    except Exception as e:
        print('Usuario no encontrado ', e)


@login_required
def administrator(request):
    products = Product.objects.all()
    users = User.objects.all()

    context = {
        'products': products,
        'users': users
    }
    return render(request, 'Botilleria/admin.html', context)

#  PRODUCTS


def Products(request):
    allProduct = Product.objects.all()
    beers = Product.objects.filter(category='Cerveza')
    wines = Product.objects.filter(category='Vino')
    whiskey = Product.objects.filter(category='Whisky')
    pisco = Product.objects.filter(category='Pisco')
    ron = Product.objects.filter(category='Ron')
    beverage = Product.objects.filter(category='Bebida')
    others = Product.objects.filter(category='Otro')
    context = {
        'allProduct': allProduct,
        'beers': beers,
        'wines': wines,
        'whiskey': whiskey,
        'pisco': pisco,
        'ron': ron,
        'beverage': beverage,
        'others': others,
    }
    return render(request, 'Botilleria/products.html', context)


@login_required
def addProduct(request):
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
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
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'Products/productDetail.html', {'product': product})
    except Exception as e:
        print('El producto seleccionado no se actualizo', e)


@login_required
def editProduct(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                messages.success(request, 'Producto modificado')
                return redirect('administrator')
        else:
            form = ProductForm(instance=product)
        return render(request, 'Products/editProduct.html', {'form': form})
    except Exception as e:
        print('producto no editado', e)


@login_required
def deleteProduct(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            product.delete()
            messages.success(request, 'Producto eliminado')
            return redirect('administrator')
        return render(request, {'product': product})
    except Exception as e:
        print('Producto no eliminado ', e)

#  CARRITO


def addCartProducts(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        cart.addProduct(product)
        messages.success(request, 'Producto agregado al carro de compras')
        return redirect('products')
    except Exception as e:
        print('No se pudo agregar producto al carrito', e)


def deleteCartProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        cart.deleteCartProduct(product)
        messages.success(request, 'Producto eliminado del carro de compras')
        return redirect('cart')
    except Exception as e:
        print('No se pudo eliminar el producto', e)


def addQuantityProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=pk)
        cart.addQuantityCartProduct(product)
        return redirect('cart')
    except Exception as e:
        print('No se pudo aumentar la cantidad', e)


def subQuantityProduct(request, pk):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=pk)
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


def saveProducts(request):
    try:
        purchaseCode = uuid.uuid4()
        if request.user.id == None:
            messages.error(
                request, 'Debes registrate antes de realizar el pago')
            return redirect('new-user')
        for key, value in request.session['cart'].items():
            products = Purchased_products(
                user_id=request.user,
                product_id=Product(value['id']),
                purchase_code=purchaseCode,
                price=value['price'],
                quantity=value['units'],
            )
            products.save()
            print(products)
            cart = Cart(request)
            cart.clearAllProducts()
            ticket = Ticket_purchase(
                purchase_product_id=Purchased_products(products.id)
            )
            ticket.save()
            messages.success(
                request, 'Haz completado tu pago, el numero de orden es: ' + str(purchaseCode))
        return redirect('home')
    except Exception as e:
        print('Productos no guardados', e)

#  USUARIOS


def signOut(request):
    messages.success(request, 'Haz terminado tu sesion...')
    logout(request)
    return redirect('home')


def newUser(request):
    try:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                )
                user.save()
                login(request, user)
                messages.success(request, 'Usuario agregado...')
                return redirect('home')
        else:
            form = UserForm()
        return render(request, 'User/newUser.html', {'form': form})
    except Exception as e:
        print('Error en user', e)


@login_required
def editUser(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            form = UserAdminForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.success(request, 'Usuario modificado')
                return redirect('administrator')
        else:
            form = UserAdminForm(instance=user)
        return render(request, 'User/editUser.html', {'form': form})
    except Exception as e:
        print('producto no editado', e)


@login_required
def deleteUser(request, pk):
    try:
        user = get_object_or_404(User, pk=pk)
        if request.method == 'POST':
            user.delete()
            messages.success(request, 'Usuario eliminado')
            return redirect('administrator')
        return render(request, {'user': user})
    except Exception as e:
        print('Producto no eliminado ', e)
