import random

class Hangman:

    """A class representing the Hangman game."""

    def __init__(self, word_list, num_lives = 5):

        """
        Initializes the Hangman game with a list of words and number of lives.
        
        Parameters:
            word_list: List of words to select from.
            num_lives: Number of lives the player starts with. Default is 5.
        """

        self._word_list = [word.lower() for word in word_list]
        self.word = random.choice(self._word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.num_lives = num_lives

        """
        Instance Variables:
            _word_list : List of words converted to lowercase for internal use.
            word: The word randomly selected from the word list for the player to guess.
            word_guessed: A list of the letters of the word, with _ for each letter not yet guessed.
            num_letters: Number of unique letters in the word that have not been guessed yet.
            num_lives: Number of lives the player has remaining.
            list_of_guesses: List of letters guessed by the player.
        """

    def _check_guess(self, guess):

        """
        This method will check if the guess is in the word. 
        The game state then updates once this occurs.
        """

        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            


    def _ask_for_input(self):

        """"
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        """

        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid response. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
              self._check_guess(guess)
              print(self.word_guessed)
              self.list_of_guesses.append(guess)
              break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The letter was {game.word}")
            break
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break
        if game.num_letters > 0:
            game._ask_for_input()


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
              