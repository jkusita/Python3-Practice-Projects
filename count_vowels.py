# Count Vowels – Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

vowel_list = ["a", "e", "i", "o", "u"]
vowel_count = 0 # Try removing this first.

# Counts the number of vowels in the inputted string.
user_input = input("Please enter a string: ")
for i in range(len(user_input)):
    if user_input[i] in vowel_list:
        vowel_count += 1

# Prints out how much vowels are in the string based on certain conditions.
if vowel_count == 0:
    print("There are no vowels.")
elif vowel_count == 1:
    print("There is only one vowel.")
else:
    print(f"There are {vowel_count} vowels.")

