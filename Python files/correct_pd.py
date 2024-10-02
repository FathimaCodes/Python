correct_password="secure123"
user_input=""
while user_input!=correct_password:
    user_input=input("Enter the password:")
    if user_input==correct_password:
        print("Access granted!")
    else:
        print("Incorrect password, try again!")