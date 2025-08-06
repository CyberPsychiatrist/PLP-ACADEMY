#Week three Assignment 
#With exception handling
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Get user input
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))
    
    # Calculate and display final price
    final_price = calculate_discount(original_price, discount)
    print(f"The final price is: Ksh.{final_price:.2f}")
    
except ValueError:
    print("Please enter valid numerical values.")