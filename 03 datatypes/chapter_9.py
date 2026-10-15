# Sets - Unique values only store
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # Union operation
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # Intersection operation
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices # Get only values which is not common in both sets
print(f"Only in essential spices: {only_in_essential}")

# Membership testing
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")