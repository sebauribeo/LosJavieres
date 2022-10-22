def totalPrice(request):
    totalCarrito = 0
    if request.session['cart']:
        for key, value in request.session['cart'].items():
            totalCarrito += int(value['total'])
    return {'totalPrice': totalCarrito}