from django.shortcuts import get_object_or_404, redirect, render
from Botilleria.cart import Cart
from Botilleria.forms import LogInForm, ProductForm, UserAdminForm, UserForm
from Botilleria.models import Product, Purchase_invoice, Purchased_products, Ticket_purchase
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timedelta
from django.db.models import Sum
import calendar
import locale
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
    try:
        products = Product.objects.all()
        users = User.objects.all()
        date_now = datetime.now()

        # Ventas diarias
        daily_purchased_products = Purchased_products.objects.filter(date=datetime.now().strftime('%Y-%m-%d'))
        daily_total_spent = sum(daily_purchased_products.price for daily_purchased_products in daily_purchased_products)
        daily_product_details = (
            Purchased_products.objects
            .filter(date=datetime.now().strftime('%Y-%m-%d'))
            .exclude(product_id__isnull=True)
            .values('product_id__name', 'product_id')
            .annotate(total_quantity=Sum('quantity'))
        )
        # Ventas mensuales
        # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Puedes ajustar el código de idioma según tu configuración
        monthly_purchased_products = Purchased_products.objects.filter(date__month=date_now.month)
        monthly_total_spent = sum(monthly_purchased_products.price for monthly_purchased_products in monthly_purchased_products)
        monthly_product_details = (
            monthly_purchased_products
            .exclude(product_id__isnull=True)
            .values('product_id__name', 'product_id')
            .annotate(total_quantity=Sum('quantity'))
        )

        context = {
            'products': products,
            'users': users,
            'daily_total_spent': daily_total_spent,
            'daily_purchased_products': daily_purchased_products,
            'daily_product_details': daily_product_details,
            'monthly_purchased_products': monthly_purchased_products,
            'monthly_total_spent': monthly_total_spent,
            'monthly_product_details': monthly_product_details,
            'date_now': date_now - timedelta(hours=3),
            'month_now': calendar.month_name[date_now.month],
        }
        return render(request, 'Botilleria/admin.html', context)
    except Exception as e:
        print('Error admin', e)
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
        if request.user.id is None:
            messages.error(request, 'Debes registrarte antes de realizar el pago')
            return redirect('new-user')
        purchase_type = request.POST.get('purchase_type')
        print(purchase_type)
        for key, value in request.session['cart'].items():
            product_id = value['id']
            quantity = value['units']
            # Obtener el objeto Product
            product = Product.objects.get(pk=product_id)
            # Crear el objeto Purchased_products por cada producto
            purchased_product = Purchased_products(
                user_id=request.user,
                product_id=product,
                purchase_code=purchaseCode,
                price=value['price'],
                quantity=quantity,
            )
            purchased_product.save()
            # Guardar en Ticket_purchase o Purchase_invoice según la elección del usuario
            if purchase_type == 'boleta':
                ticket = Ticket_purchase(purchase_product_id=purchased_product)
                ticket.save()
            elif purchase_type == 'factura':
                invoice = Purchase_invoice(purchase_product_id=purchased_product)
                invoice.save()
            # Actualizar el stock del producto
            product.stock -= quantity
            product.save()

        # Limpiar el carrito después de realizar la compra
        cart = Cart(request)
        cart.clearAllProducts()

        messages.success(request, 'Has completado tu pago, el número de orden es: ' + str(purchaseCode))
        return redirect('home')
    except Exception as e:
        print('Productos no guardados', e)
        messages.error(request, 'Error al procesar la compra. Por favor, inténtalo de nuevo.')
        return redirect('cart')


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
