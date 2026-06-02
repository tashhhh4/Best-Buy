from products import Product

""" Best Buy - store.py """


class Store:
    """ The store tracks a list of products that belong to it. """

    def __init__(self):
        """ Initializes the Store with an empty Product list. """
        self.products = []

    def add_product(self, product):
        """ Adds a Product to the Store. """
        self.products.append(product)

    def remove_product(self, product):
        """ Removes the Product from the Store. """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """ Returns a count of the total number of items (of all Products) in the Store. """
        count = 0
        for product in self.products:
            count += product.get_quantity()
        return count

    def get_all_products(self) -> List[Product]:
        """ Returns a list of all Products (only active) in the Store. """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        """ Processes a purchase order for the Store.

            Returns:
                total :: The total price of the order

            Args:
                shopping_list :: tuple(Product, quantity)
        """
        total = 0
        for product, quantity in shopping_list:
            cost = product.buy(quantity)
            total += cost
        return total


# Tests
if __name__ == "__main__":
    try:
        # Create Store
        my_store = Store()
        assert len(my_store.get_all_products()) == 0

        # Add Products
        p1 = Product("Product 1", 10.99, 10)
        p2 = Product("Product 2", 25.99, 5)

        my_store.add_product(p1)
        my_store.add_product(p2)

        # Get all Products
        assert len(my_store.get_all_products()) == 2
        assert p2 in my_store.get_all_products()

        # Remove Products
        my_store.remove_product(p2)

        # Test buying function
        price = my_store.order([(p1, 2)])
        assert price == 10.99 * 2

        # Count total quantity
        assert my_store.get_total_quantity() == 8

        print("All tests passed.")

    except Exception as e:
        print("Test failed...")
        print(e)