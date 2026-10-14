# String, Indexing and Slicing
chai_type = "Ginger Chai"
customer_name = "Amandeep Singh"

print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}") # StartIndex:EndIndex:Stepper
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}") # Reverse the string

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")