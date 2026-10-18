# Hiding the details
def get_input():
    print("Get the input data")

def validate_input():
    print("Validating the input data")

def save_to_db():
    print("Saving the user to db")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered successfully!")

register_user()