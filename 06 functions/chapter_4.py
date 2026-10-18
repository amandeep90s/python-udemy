# Readability
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

myBill = calculate_bill(5, 10)
print(f"My total bill: {myBill}")

print(f"Bill for table 2: {calculate_bill(5, 23)}")