seat_type = input("Enter the seat type (sleeper, general, AC, luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, Beds are available")
    case "ac":
        print("AC is available")
    case "general":
        print("Cheapest option")
    case "luxury":
        print("Meal is available")
    case _:
        print("Invalid seat type")
