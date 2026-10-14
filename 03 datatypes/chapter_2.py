# Object values are mutable but their id is immutable

spice_mix = set()
print(f"Initial spice_mix id: {id(spice_mix)}")
print(f"Initial spice_mix value: {spice_mix}")

spice_mix.add('Lemon')
spice_mix.add('Ginger')
spice_mix.add('Garlic')

print(f"After adding spices spice_mix id: {id(spice_mix)}")
print(f"After adding spices spice_mix value: {spice_mix}")