import random

# Guess the number game i saw in a book

number = random.randint(1, 10) + 1

while True:
    p = int(input("Please guess the number between 1 - 10 : "))
    if p > number:
        print("The number is smaller, guess again")
        print()
    elif p < number:
        print("The number is bigger, guess again")
        print()
    elif p == number:
        print("Bingo!!! Correct guess.")
        break
