def delivery_fee(distance, rate):
    return distance * rate

# Get user input
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

# Calculate total fee
total = delivery_fee(distance, rate)

# Display the result
print(f"Total Delivery Fee: ₱{total:.2f}")