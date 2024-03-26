def calculate_selling_price(cost_price, markup_percent):
    markup_decimal = markup_percent / 100
    selling_price = cost_price * (1 + markup_decimal)
    return selling_price

supplier_cost= float(input("Enter the cost price from the supplier: "))
markup_perecentage = 10

selling_price = calculate_selling_price(supplier_cost, markup_perecentage)
print(f"Selling price: Rp. {selling_price:,}")