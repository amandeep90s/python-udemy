# Tuples

masala_spices = ("cinnamon", "cloves", "cardamom")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Radio of ginger: {ginger_ratio} and cardamom: {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Radio of ginger: {ginger_ratio} and cardamom: {cardamom_ratio}")

# membership testing
# Case sensitive
print(f"Is cinnamon in masala spices? {"cinnamon" in masala_spices}")
