"""
Number Guessing Game
Guess a random number between 1 and 100.
"""
import random
number=random.randint(1,100)
attempts=0
print("Welcome to the guessing game.")
print("guess a number between 1 and 100.")

while True:
    try:
        guess=int(input("Enter a guess number."))
        attempts+=1
        if guess<number:
            print("The target is too low, try again for a bigger number.")
        elif guess>number:
            print("The target is too high, try again for a smaller number.")
        elif guess==number:
            print(f"Congratulation! You won the game in {attempts} attempts.")
            break
    except ValueError:
        print("Invlaid number! Please enter a valid number.")             
