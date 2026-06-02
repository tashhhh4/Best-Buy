""" Best Buy - store.py """


class Store:
    """ The store tracks a list of products that belong to it. """

    def __init__(self):
        """ Initializes the Store with an empty Product list. """
        self.products = []

    def add_product(self, product):
        """ Adds a Product to the Store. """
        pass

    def remove_product(self, product):
        """ If the Product exists in the Store,
        removes it.
        """
        pass

    def get_total_quantity(self) -> int:
        """ Returns a count of the total number of items (of all Products) in the Store. """
        pass

    def get_all_products(self) -> List[Product]:
        """ Returns a list of all Products (only active) in the Store. """
        pass

    def order(self, shopping_list) -> float:
        """ Processes a purchase order for the Store.

            Returns:
                total :: The total price of the order

            Args:
                shopping_list :: tuple(Product, quantity)
        """
        pass


# Tests
if __name__ == "__main__":
    pass