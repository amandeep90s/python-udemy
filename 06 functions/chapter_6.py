# Scopes

chai_type = "Ginger" # Global scope

def chai_order():
    chai_type = "Mint" # Local scope
    print(f"Inner function: {chai_type}")

chai_order()
print(f"Outer function: {chai_type}")

# Nested functions scope
chai = "Tulsi"
def chai_counter():
    chai = "Masala" # Enclosing scope
    def inner_func():
        chai = "Rose"
        print('Inner func:', chai)
    inner_func()
    print('Chai counter func:', chai)
chai_counter()
print('Outer func:', chai)