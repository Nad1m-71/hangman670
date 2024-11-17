import random

list_of_fruits = ["Apple", "Mango", "Pineapple", "Pear", "Watermelon"]

random_fruit = random.choice(list_of_fruits)

def check_guess(guess):
    guess = guess.lower()
    if guess in random_fruit:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha:
            check_guess(guess)
            break
        else:
            print("invalid letter. Please, enter a single alphabetical character.")

ask_for_input()
