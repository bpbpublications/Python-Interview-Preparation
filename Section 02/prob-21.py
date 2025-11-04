class Item:
    def __init__(self, name, price):
        # Each item has a name, price, and initial quantity
        self.name = name
        self.price = price
        self.quantity = 1
 
class Cart:
    def __init__(self):
        # Initialize the cart with an empty dictionary of items
        self.items = {}
 
    def add_item(self, item, quantity=1):
        # Add an item to the cart, or update the quantity if it already exists
        if item.name in self.items:
            self.items[item.name].quantity += quantity
        else:
            item.quantity = quantity
            self.items[item.name] = item
 
    def remove_item(self, item_name):
        # Remove an item from the cart by its name
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item {item_name} not found in cart.")
 
    def view_cart(self):
        # Display all items in the cart, their quantities, and total price
        if not self.items:
            print("The cart is empty.")
            return
        print("Cart:")
        for item in self.items.values():
            print(f"- {item.name}: {item.quantity} @ ${item.price} each")
        print(f"Total cost: ${self.total_cost()}")
 
    def total_cost(self):
        # Calculate and return the total cost of all items in the cart
        total = 0
        for item in self.items.values():
            total += item.price * item.quantity
        return total
