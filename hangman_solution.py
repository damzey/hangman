'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
from ctypes.wintypes import WORD
from curses.ascii import isalpha
from lib2to3.pytree import LeafPattern
from mimetypes import guess_all_extensions
import random
from site import getuserbase
from threading import Thread
from tkinter import Y

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
    self.word_list = word_list
    self.num_lives = num_lives
    self.word_guessed = word_guessed
    self.list_letters = list_letters
    self.word = word
    self.game_over = False
    self.num_letters = len(set(self.word))

def hangman():     
    list_letters = []
    correct_letter = []
    num_letters = len(word)
    num_lives = 5
    guessed = False
    word_guessed = "_"*len(word)
    alphabet = [abcdefghijklmnopqrstuvwxyz]	
    blanks_list = list(word_guessed) 
    new_blanks_list = list(word_guessed)
    game_is_done = False
        

def get_word(): 
    word = random.choice(word_list) 
    return word.lower()

def win():
    if "_" not in guessed_letters:
        print("You have won")

def playAgain():
    play_again = input("Play again? (Y/N?").lower() 

def printed_scaffold():
        

        # TODO 2: Initialize the attributes as indicated in the docstring
        
def hangman_intro:    # TODO 2: Print two message upon initialization:
    print(f"The mystery word has {len(self.word)} characters")
    print{self.word_guessed}
    pass

def check_letter(self, letter) -> None:
    while not guessed and num_lives > 0:
        if letter.lower() in self.word:
          print (f"Good job, {letter} is in the word")
          correct_letter.append(letter)
          list_letter.append(letter)
          num_letters -= 1
            for i in range(len(self_word)):
                self.word_guessed[i] = letter.lower()
                print(guessed_letters)
                printed_scaffold(num_lives)
                if "_" not in guessed_letters:
                  guessed = True
                  game_is_done = True
                  print("Congratulations, you won")
        else:
            print(f"Sorry,{letter} is not in the word")
            num_lives -= 1
            list_letter.append(letter)
            print("You have {num_lives} lives left")
            printed_scaffold(num_lives)
            print(num_lives)
            print(guessed_letters)
            if num_lives > 0:
                print("Guess again")
            elif num_lives == 0: 
                print(f"You ran out of lives. the word was {word}")
            else:
                print()
        if guessed == True or num_lives == 0:
            playAgain()
            while play_again == "y":
                play_game(word_list)
            else:
                print("Thank you for playing. Until next time")
        
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        

        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A word can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

def ask_letter(self): #asks the user to input a valid letter
    num_lives = num_lives
    while not guessed and num_lives > 0 : 
        letter = input("Please guess a letter:") #asking the user for a letter guess
        letter = guess.lower()
        letter = str(letter) #converting the letter to a string
      if letter not in alphabet:
        print ("Please enter a  valid letter")
      elif letter in list_letters:
        print (f"{letter} was already tried. Choose again")
      elif if len(letter) != 1:
        print("Please enter a SINGLE letter")
      else:
        pass
check_letter()

        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method


def play_game(word_list):
    
    game = Hangman(word_list, num_lives=5)
    game = Hangman(word_list)
    hangman_intro()
    word = get_word()
    game.ask_letter()
    pass



    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
