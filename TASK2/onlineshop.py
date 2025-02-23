class CartItem:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        """Update the quantity of the item in the cart"""
        if quantity > 0:
            self.quantity = quantity
            print(f'Updated "{self.item_name}" quantity to {self.quantity}.')
        else:
            print("Quantity must be greater than zero.")

    def calculate_total(self):
        """Calculate total price for this item"""
        return self.price * self.quantity

    def show_info(self):
        """Return item details"""
        return f'Item: {self.item_name}, Price: ${self.price:.2f}, Quantity: {self.quantity}, Total: ${self.calculate_total():.2f}'


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the cart"""
        for item in self.items:
            if item.item_name == item_name:
                item.update_quantity(item.quantity + quantity)
                return
        self.items.append(CartItem(item_name, price, quantity))
        print(f'Added "{item_name}" to the cart.')

    def remove_item(self, item_name):
        """Remove an item from the cart"""
        for item in self.items:
            if item.item_name == item_name:
                self.items.remove(item)
                print(f'Removed "{item_name}" from the cart.')
                return
        print(f'Item "{item_name}" not found in cart.')

    def calculate_total(self):
        """Calculate the total cost of all items in the cart"""
        return sum(item.calculate_total() for item in self.items)

    def show_cart(self):
        """Display all items in the cart"""
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\n-- Shopping Cart --")
            for item in self.items:
                print(item.show_info())
            print(f'Total Cart Value: ${self.calculate_total():.2f}')


# Main Menu
cart = ShoppingCart()

while True:
    print("\n-- Online Shopping Cart Menu --")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        cart.show_cart()

    elif menu == "2":
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        cart.add_item(item_name, price, quantity)

    elif menu == "3":
        item_name = input("Enter item name to remove: ")
        cart.remove_item(item_name)

    elif menu == "4":
        cart.show_cart()
        print("Proceeding to checkout... Thank you for shopping!")
        break

    elif menu == "5":
        print("Exiting... Have a great day!")
        break

    else:
        print("Invalid selection. Please choose a valid option.")
