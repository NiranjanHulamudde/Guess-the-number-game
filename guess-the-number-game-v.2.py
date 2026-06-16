import random

# Guess the number game i saw in a book


while True:
    try:
        number = random.randint(1, 10)

        p = int(input("Please guess the number between 1 - 10 : "))
    except ValueError:
        print("Please enter whole numbers only ")
        continue
    if p > 10 or p < 1:
       print("Please select a number between 1-10")
       continue
    elif p > number:
        print("The number is smaller, guess again")
        print()
    elif p < number:
        print("The number is bigger, guess again")
        print()
    elif p == number:
        print("Bingo!!! Correct guess.")
        try:
            ask = (input("Would you like to continue, y/n? "))
        except NameError:
            print("Please choose between y/n only. ")
            continue
        if ask == "y":
            continue
        elif ask == "n":
            break
    
