def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Prompt the user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"Final price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
