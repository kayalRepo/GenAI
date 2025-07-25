# ShoppingBill.py
def calculate_total(prices, tax_percent):
    subtotal = sum(prices)
    tax = subtotal * (tax_percent / 100)
    return subtotal + tax

# Example usage
items = [float(input(f"Enter price for item {i+1}: ")) for i in range(3)]
tax = float(input("Enter tax percentage: "))
print("Total cost including tax:", calculate_total(items, tax))
