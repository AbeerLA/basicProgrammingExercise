def calculate_selling_price(cost_price):
    # Calculate selling price as 10% more than cost price
    selling_price = cost_price * 1.10
    return selling_price

# Main function to run the application
def main():
    # Input the cost price from the user
    cost_price = float(input("Enter the cost price of the item: "))

    # Calculate the selling price
    selling_price = calculate_selling_price(cost_price)

    # Display the selling price
    print(f"The selling price of the item is: ${selling_price:.2f}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
