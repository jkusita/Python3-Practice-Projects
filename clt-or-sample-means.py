# Tests statistics thing (central limit theorem or mean of sample means?) I don't even know lol.

import random, time



one_list = 0
two_list = 0
three_list = 0
four_list = 0
count = 0

number_of_rolls = int(input("How many dice rolls?: "))
while True:
    dice_number = random.randint(1, 4)
    print(dice_number)
    if dice_number == 1:
        one_list += 1
    elif dice_number == 2:
        two_list += 1
    elif dice_number == 3:
        three_list += 1
    else:
        four_list += 1
    
    count += 1
    if count == number_of_rolls:
        print(f"Number of 1's: {one_list}, Percentage: {one_list/10000}")
        print(f"Number of 2's: {two_list}, Percentage: {two_list/10000}")
        print(f"Number of 3's: {three_list}, Percentage: {three_list/10000}")
        print(f"Number of 4's: {four_list}, Percentage: {four_list/10000}")
        break


