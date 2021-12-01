"""A number-guessing game."""
# Luba and Ruchi huessing game task
import random
    

def guess_game ():
   ## ask for name from console
    name = input("What is your name?")
    print(name + ", I am thinking of a number between 1 and 100.")
    print("Try to guess the number.")

    ## number of tries
    tries = 0

    ## generating random number
    secret_number = random.randint(1, 100)
    print(secret_number)
    # ask user quess number
    user_guess = None

    while secret_number != user_guess:
        user_guess = int(input("Your guess? "))

        if 100 < user_guess or user_guess < 0:
            print("please enter valid number")

        elif 0 < user_guess < secret_number:
            print("The number is too low, try again!")
            tries += 1
        elif secret_number < user_guess < 100:
            print("The number is too high, try again!")
            tries += 1

    else:
        print(f'Well done, {name}! You found my number in  {tries} tries')
        

guess_game()
