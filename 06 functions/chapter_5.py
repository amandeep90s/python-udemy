# Traceability
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 300, 500]

for price in orders:
    total_amount = add_vat(price, 18)
    print(f"Original price: {price}, Final with VAT: {total_amount}")