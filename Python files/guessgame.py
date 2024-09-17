import random
number_to_guess= random.randint(1,100)
user_guess=int(input("Guess the number (between 1 and 100):"))
if user_guess<number_to_guess:
    print("Too low! Try again.")
elif user_guess>number_to_guess:
    print("Too high! Try again.")
else:
    print("Congratulations! You guessed the number correctly.")
if user_guess != number_to_guess:
    print(f"The correct number was {number_to_guess}.")
