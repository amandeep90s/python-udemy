# Walrus operator

# First example
value = 13
if remainder := value % 5:
    print(f"Value is not divisible by {value}: {remainder}")

flavours = ["masala", "mint", "lemon", "rose"]
print(f"Available flavours: {flavours}")

# Second example
while (flavour := input("Which flavour do you prefer to buy: ")) not in flavours:
    print(f"Sorry flavour {flavour} is not available")

print(f"You choose: {flavour} chai")

# Third example
cup_sizes = ["small", "medium", "large"]
if (requested_size := input("Which size do you prefer to buy: ")) in cup_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"{requested_size} Size is not available")