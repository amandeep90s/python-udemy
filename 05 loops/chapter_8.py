candidates = [("Raj", 12), ("Aman", 36), ("John", 34)]

# For else
for name, age in candidates:
    if age >= 18:
        print(f"{name} is {age} years old.")
        break
else:
    print("Sorry, you are not allowed to do that.")