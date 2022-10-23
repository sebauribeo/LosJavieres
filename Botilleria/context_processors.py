def totalPrice(request):
    totalCarrito = 0
    if 'cart' in request.session:
        for key, value in request.session['cart'].items():
            totalCarrito += int(value['price'])
    return {'totalPrice': totalCarrito}
