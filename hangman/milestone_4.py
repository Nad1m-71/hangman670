import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = [word.lower() for word in word_list]
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.num_lives = num_lives

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            next_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {next_lives} lives left.")
            self.num_lives = next_lives

           

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid response. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
              self.check_guess(guess)
              print(self.word_guessed)
              self.list_of_guesses.append(guess)
            if self.num_letters == 0:
                print("Congrats! You have guessed the word correctly :)")
                break
            if self.num_lives == 0:
                print(f"You have ran out of lives. The word to be guess is {self.word}.")
                break



game = Hangman(["Apple", "Mango", "Pineapple", "Pear", "Watermelon"])
game.ask_for_input()
              