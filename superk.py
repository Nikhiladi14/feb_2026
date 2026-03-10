

# Store Details
STORE_NAME = "N-SUPER MARKET"
LOCATION = "Chennai"
# TAX_RATE = 0.12   # 12% tax

# Product Catalog
products = {
    "Rice": 50,
    "Sugar": 40,
    "Milk": 25,
    "Bread": 30,
    "Eggs": 6,
    "Oil": 120,
    "Soap": 35
}

cart = {}

# -------------------------------
# Function to display products
# -------------------------------
def display_products():
    print("\nAvailable Products:")
    print("-" * 30)
    for item, price in products.items():
        print(f"{item:10} : ₹{price}")
    print("-" * 30)


# -------------------------------
# Main Program
# -------------------------------
print("=" * 50)
print(STORE_NAME.center(50))
print(LOCATION.center(50))
print("=" * 50)

customer_name = input("Enter Customer Name: ")

while True:
    display_products()
    
    choice = input("\nEnter product name to add (or type 'exit' to finish): ").title()
    
    if choice.lower() == "exit":
        break
    
    if choice in products:
        try:
            quantity = int(input("Enter quantity: "))
            
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            
            if choice in cart:
                cart[choice] += quantity
            else:
                cart[choice] = quantity
                
            print(f"{choice} added to cart.")
        
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    
    else:
        print("Product not found. Please select from list.")


# -------------------------------
# Billing Section
# -------------------------------
print("\n" + "=" * 50)
print("N-SUPER MARKET".center(50))
print("RECEIPT".center(50))
print("=" * 50)

print(f"Customer Name : {customer_name}")
print("-" * 50)
print(f"{'Item':10} {'Qty':5} {'Price':10} {'Total':10}")
print("-" * 50)

subtotal = 0

for item, quantity in cart.items():
    price = products[item]
    total_price = price * quantity
    subtotal += total_price
    
    print(f"{item:10} {quantity:<5} ₹{price:<9} ₹{total_price:<10}")

# tax = subtotal * TAX_RATE
grand_total = subtotal

print("-" * 50)
print(f"{'Subtotal':30} ₹{subtotal:.2f}")
# print(f"{'Tax (12%)':30} ₹{tax:.2f}")
print(f"{'Grand Total':30} ₹{grand_total:.2f}")
print("=" * 50)

print("\nThank you for shopping with us!")
print("Visit Again 😊")
print("-" * 50)