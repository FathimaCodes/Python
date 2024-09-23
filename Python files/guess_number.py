import random
def guess_the_number(secret_number):
    while True:
        guess=int(input("Guess the number:"))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Try again! The secret number is higher.")
        else:
            print("Try again! The secret number is lower.")
secret_number= random.randint(1,100)
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")
guess_the_number(secret_number)