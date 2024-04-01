def calculate_discount(total_cost):
    if total_cost > 100:
        discount = total_cost * 0.10
    elif total_cost > 50:
        discount = total_cost * 0.05
    else:
        discount = 0
    return discount

# Input
total_cost = float(input("Enter the total cost of purchase: $"))

# Calculate discount
discount = calculate_discount(total_cost)

# Calculate total cost after discount
total_cost_after_discount = total_cost - discount

# Print result
print("Total cost after applying discount: $".format(total_cost_after_discount))
