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


# Menu functions
def list_products():
    print("Running function list_products")    

def show_product_count():
    print("Running function show_product_count")    

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
        print("   Store")
        print("   -----")
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