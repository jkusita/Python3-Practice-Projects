# Dice rolling simulator

import random, time

while True:
    dice_number = random.randint(1, 6)
    print("The dice is rolling...")
    time.sleep(2)
    print(f"You rolled {dice_number}!")
    user_input = input("Would you liket o roll again? (yes or no): ")
    if user_input.lower() == "no":
        break