import random
import lib
from replit import clear
import string

print(" Welcome to Hangman Game")
print(lib.logo)
# Generate a Random word
word = random.choice(lib.WORDS)
print(word)
# print(type(word))
size = len(word)
my_list = ['_']*size

print(f"Please Guess the word. Please note the world will have {size} characters")
print(my_list)
choice = 5

game_is_finished = False
display = []
for _ in range(size):
    display += "_"

while not game_is_finished:

    guessed_letter = input("Enter the any letter in the Guessed word\n")
    clear()
    if guessed_letter in word:
        print(f" Your guessed letter \'{guessed_letter}\' Letter there in the word")
        print("Guess the next letter")
    for position in range(size):
        letter = word[position]
        if letter == guessed_letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guessed_letter not in word:
        print("Letter not the in the list")
        choice = choice - 1
        print(f"You have {choice}  choices left")
        print(lib.stages[choice])
        if choice == 0:
            game_is_finished = True
            print("You lose.")
    if not "_" in display:
        game_is_finished = True
        print("You win.")