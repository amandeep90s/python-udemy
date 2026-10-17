flavours = ["Tulsi", "Out of Stock", "Lemon", "Masala", "Discontinued", "Rose"]

# Continue and break
for flavour in flavours:
    if flavour.lower() == "out of stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"Flavour found: {flavour}")
print("Out from the loop")