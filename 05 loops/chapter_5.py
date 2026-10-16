names = ["Mark", "John", "Billy", "Steve", "Jonson"]
bills = [290, 450, 500, 590, 276]

# Order also matters
for name, bill in zip(names, bills):
    print(f"{name} paid {bill} rupees")
