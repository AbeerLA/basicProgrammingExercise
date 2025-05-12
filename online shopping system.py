# Custom error classes
class OutOfStockError(Exception):
    pass

class InvalidPaymentError(Exception):
    pass

class EmptyCartError(Exception):
    pass

# Shop system
class OnlineShop:
    def __init__(self):
        self.inventory = {
            "laptop": 5,
            "headphones": 10,
            "mouse": 3
        }
        self.cart = {}

    def add_to_cart(self, item, quantity):
        if item not in self.inventory:
            raise OutOfStockError(f"{item} is not sold in this shop.")
        if self.inventory[item] < quantity:
            raise OutOfStockError(f"Not enough {item} in stock.")
        self.cart[item] = self.cart.get(item, 0) + quantity
        print(f"Added {quantity} {item}(s) to cart.")

    def checkout(self):
        if not self.cart:
            raise EmptyCartError("Your cart is empty. Add items before checkout.")
        total = 0
        for item, quantity in self.cart.items():
            price = 100 if item == "laptop" else 50 if item == "headphones" else 25
            total += price * quantity
        print(f"Total amount due: ${total}")
        return total

    def pay(self, amount, total_due):
        if amount < total_due:
            raise InvalidPaymentError(f"Insufficient payment. You still owe ${total_due - amount}")
        print("Payment successful. Thank you for shopping!")

# Example usage
shop = OnlineShop()

try:
    shop.add_to_cart("laptop", 2)
    shop.add_to_cart("mouse", 1)
    total_due = shop.checkout()
    shop.pay(300, total_due)

except OutOfStockError as e:
    print("Stock error:", e)
except EmptyCartError as e:
    print("Cart error:", e)
except InvalidPaymentError as e:
    print("Payment error:", e)
