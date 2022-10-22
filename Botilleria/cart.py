class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            self.cart = self.session['cart']
        else:
            self.cart = cart

    def addProduct(self, product):
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

    def saveCart(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    
    def deleteCart(self, product):
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.saveCart()

    def restar(self, product):
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]['units'] -= 1
            self.cart[id]['price'] -= product.price
            self.saveCart()

    def suma(self, product):
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]['units'] += 1
            self.cart[id]['price'] += product.price
            self.saveCart()

    def clean(self):
        self.session['cart'] = {}
        self.session.modified = True
