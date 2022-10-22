class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        try:
            if not cart:
                self.session['cart'] = {}
                self.cart = self.session['cart']
            else:
                self.cart = cart
        except Exception as e:
            print('Error', e)

    def addProduct(self, product):
        try:
            id = product.id
            if id not in self.cart.keys():
                self.cart[id] = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'brand' : product.brand,
                    'units': 1,
                } 
            self.saveCart()
            print('Producto agregado al carrito', e)
        except Exception as e:
            print('Producto no agregado', e)

    def saveCart(self):
        try:
            self.session['cart'] = self.cart
            self.session.modified = True
            print('Producto guardado en carrito')
        except Exception as e:
            print('Producto no guardado', e)
    
    def deleteCartProduct(self, product):
        try:
            id = str(product.id)
            if id in self.cart:
                del self.cart[id]
                self.saveCart()
            print(0)
        except Exception as e:
            print('producto no editado', e)

    def subQuantityCartProduct(self, product):
        try:
            id = str(product.id)
            if id in self.cart.keys():
                self.cart[id]['units'] -= 1
                self.cart[id]['price'] -= product.price
                if self.cart[id]["units"] <= 0: self.deleteCartProduct(product)
                self.saveCart()
            print('Cantidad agregada al producto')
        except Exception as e:
            print('No se pudo aumentar la cantidad', e)

    def addQuantityCartProduct(self, product):
        try:
            id = str(product.id)
            if id in self.cart.keys():
                self.cart[id]['units'] += 1
                self.cart[id]['price'] += product.price
                self.saveCart()
            print('Se disminuyo la cantidad del producto')
        except Exception as e:
            print('No se disminuyo la cantidad del producto', e)

    def clearAllProducts(self):
        try:
            self.session['cart'] = {}
            self.session.modified = True
            print('Carrito limpiado')
        except Exception as e:
            print('No se pudo limpiar el carrito', e)
