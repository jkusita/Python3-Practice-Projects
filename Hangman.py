# A program like the Hangman game.

import random
from random_word import RandomWords

r = RandomWords()

# Dont' hardcode
# get the length of the string that is picked from the pre-made list.
# Don't make your music too high, make it background/low music so you don't get irritated by the song.
# cmd + L: highlights a whole line.
# Break it down to smaller problems (the smallest it can be) (one step at a time)

answer = r.get_random_word()
answer_list = list(answer)
len_answer = len(answer)

print(f"Word: {answer}") # for testing

# Makes a list that contains underscores for design.
underscore_list = []
for i in range(len_answer):
    underscore_list.append("_")
# underscore_list_join = "".join(underscore_list)
# Replace the underscores with the correct answers 


# How many guesses do you get per len of string?
number_of_guess = len_answer + int(len_answer/2)
print(f"Length: {len_answer}")
print(f"# of guesses: {number_of_guess}")

# Comment here
# print(answer_list) # for testing
# print(underscore_list_join) # for testing

# What happens if there are two of the same character guessed?
# What happens if you guess a letter that's been guessed already?

while number_of_guess != 0:
    print(f"\nYou have {number_of_guess} guesses.") # subtract this by one for every guess.
    number_of_guess -= 1
    user_guess = input("Enter a character: ")
    if user_guess in answer_list:
        print("Correct")
        while user_guess in answer_list:
            # Gets the index of the user's guess from the answer_list.
            answer_list_index = answer_list.index(user_guess)
            # Replaces the corresponding underscore to the user's guess.
            underscore_list[answer_list_index] = user_guess
            # Removes the user's guess from the answer_list (this is useful if there are more than one same characters).
            answer_list[answer_list_index] = None
        underscore_list_join = "".join(underscore_list)
        print(underscore_list_join)
    else:
        print("Wrong")
    

