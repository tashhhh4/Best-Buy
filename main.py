""" Best Buy - main.py """

import products
import store

# Setup initial store and products
product_list = [
    products.Product("Macbook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)


# Console helper functions
def print_divider():
    """ Prints a divider to help visually space the UI. """
    print("------")

def print_title():
    """ Prints the main title/header of the program. """
    print("   Store Menu")
    print("   ----------")


# Menu functions
def list_products():
    print_divider()
    products = best_buy.get_all_products()
    if not products:
        print("Store inventory is empty!")
    else:
        for product in products:
            product.show()
    print_divider()

def show_product_count():
    num_items = best_buy.get_total_quantity()
    print(f"Total of {num_items} items in the store") 

def make_order():
    print("Running function make_order")    


def start(store):
    """ Displays a console menu to the user and allows
    interaction with the main Store. """

    # Menu choices
    choices = [
        ("List all products in the store", list_products),
        ("Show total amount in store", show_product_count),
        ("Make an order", make_order),
        ("Quit",),
    ]

    # Menu Main Loop
    while True:
        print()
        print_title()
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice[0]}")

        try:
            user_choice = int(input("Please enter a number: ").strip())

            if user_choice == len(choices): # Quit signal received
                break

            if not 1 <= user_choice <= len(choices):
                print("Invalid choice! Please try again.")
                continue

            choices[user_choice - 1][1]()

        except ValueError:
            print("Invalid choice! Please try again.")
            continue


if __name__ == "__main__":
    start(store)