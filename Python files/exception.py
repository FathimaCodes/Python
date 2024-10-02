def get_number():
    while True:
        try:
            user_input= input("Please enter a number:")
            number= float(user_input)
            print(f"You entered the number: {number}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
get_number()