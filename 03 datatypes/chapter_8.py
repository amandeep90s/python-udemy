# Mutables
# List type actually know as array in other languages
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
# Merging two lists
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea") # add new value in index 2 and moved other values to right side
print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"Chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
