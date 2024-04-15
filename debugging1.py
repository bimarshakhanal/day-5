class Product:
    '''Class representing a product.'''

    def __init__(self, name, price, quantity):
        '''Initialize a product with a name, price, and quantity.'''
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        '''Calculate and return the total price of the product.'''
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        '''Update the quantity of the product.'''
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")


class ShoppingCart:
    '''Class representing a shopping cart.'''

    def __init__(self):
        '''Initialize a shopping cart with an empty list of products.'''
        self.products = {}

    def add_product(self, product, quantity):
        '''Add a product to the shopping cart with a specified quantity.'''
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        '''Remove a product from the shopping cart with a specified quantity.'''
        if product in self.products:
            if self.products[product] <= quantity:
                del self.products[product]
            else:
                self.products[product] -= quantity
        else:
            print("Product not found in the cart.")

    def get_total_cart_price(self):
        '''Calculate and return the total price of the products in the shopping cart.'''
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_total_price() * quantity
        return total_price


class Customer:
    '''Class representing a customer.'''

    def __init__(self, name, email):
        '''Initialize a customer with a name, email, and an empty shopping cart.'''
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        '''Add a product to the customer's shopping cart with a specified quantity.'''
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        '''Remove a product from the customer's shopping cart with a specified quantity.'''
        self.shopping_cart.remove_product(product, quantity)

    def checkout(self):
        '''Checkout the items in the customer's shopping cart.'''
        total_price = self.shopping_cart.get_total_cart_price()
        if total_price > 0:
            print(f"Checking out... Your total is ${total_price}.")
            self.shopping_cart.products = {}
        else:
            print("Your cart is empty. Nothing to checkout.")


# Test the e-commerce system
product1 = Product("Keyboard", 50, -2)
product2 = Product("Mouse", 30, 3)

customer = Customer("John Doe", "john.doe@example.com")
customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)
customer.checkout()

customer.add_to_cart(product1, -1)
customer.remove_from_cart(product2, 3)
