class CashRegister:
    def __init__(self):
        # Initialize an empty dictionary to store items and prices
        self.items = {}
        self.discount = 0
 
    def add_item(self, item_name, price):
        # Add an item to the cart
        self.items[item_name] = price
 
    def apply_discount(self, discount):
        # Apply a discount percentage to the total bill
        self.discount = discount
 
    def calculate_total(self):
        # Calculate the total amount with the discount applied
        total = sum(self.items.values())
        if self.discount > 0:
            total = total - (total * self.discount / 100)
        return total
 
    def display_items(self):
        # Display all items, their prices, and the total with discount
        print("Items in cart:")
        for item_name, price in self.items.items():
            print(f"{item_name}: ${price:.2f}")
        if self.discount > 0:
            print(f"Discount applied: {self.discount}%")
        total = self.calculate_total()
        print(f"Total: ${total:.2f}")
