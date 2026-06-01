""" Best Buy - products.py """

class Product:
    """ A product in the store inventory. """

    def __init__(self, name, price, quantity):
        """ Sets the data and initial quantity and active state of the product.
        All fields required.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """ Returns the current quantity of this product. """
        pass

    def set_quantity(self, quantity):
        """ Updates the quantity of this product. """
        pass

    def is_active(self) -> bool:
        """ Reports if this product is active (visible). """
        pass

    def activate(self):
        """ Sets this product's status to active (`True`). """
        pass

    def deactivate(self):
        """ Sets this product's status to inactive (`False`). """
        pass

    def show(self):
        """ Prints an string representation of the product containing all of its basic info. """
        pass

    def buy(self, quantity) -> float:
        """ 'Buys' a product. Returns the total price given the desired quantity,
        and deducts the product from the store's total inventory. """
        pass


# Run tests on the Product class
if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    
    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()