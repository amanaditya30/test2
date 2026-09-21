def calculate_discount(price):
    discount = price * 0.20
    final_price = price + discount
    return final_price


price = 100
result = calculate_discount(price)

print("Final price:", result)
