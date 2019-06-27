# Guess the number program

import random

# Generates the number to be guessed.
random_number = random.randint(0, 100)

while True:
    user_guess = int(input("Guess the number!: "))

    # Checks if the user gets it correct or is too high/low.
    if user_guess == random_number:
        print(f"The number {user_guess} is right!")
        break
    else:
        if user_guess > random_number:
            print(f"Wrong, the number {user_guess} is too high!")
        else:
            print(f"Wrong, the number {user_guess} is too low!")
