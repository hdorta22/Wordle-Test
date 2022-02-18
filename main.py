"""
Ethan Gonzalez
Alejandro Madrigal
Daniel Gonzalez
Hugo Dorta
Wordle Test
Due: 2/25/22
"""
"""
grey-incorrect, letter is not in word
yellow-semi, letter is in the word but is not in correct spot
green-correct, Letter is in word and in correct spot
"""

from oxford import Word

from art import tprint
import os
tprint("WORDLE", "Boxing")

# Takes in a string
def word_exist(word):
    try:
        Word.get(word)
        return


if word_exist(word) == True:
  break
else word_exist(word) == False:
  word = input("Enter a reference word: ")
  print(word_exist(word))

def break_code():
    while True:
        print("Type '22' if you want to exit!")
        what = input(f"Guess: ")
        if(what == "22"):
            break
"""

option_list = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


"""