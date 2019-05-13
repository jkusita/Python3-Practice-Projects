# Count Vowels – Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

vowel_list = ["a", "e", "i", "o", "u"]
vowel_count = 0 # Change this so it adds all the values of the keys in the new dictionary.
vowel_count_found = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0} # TODO: maybe you can change the keys from strings to variable (if possible)?
# vowel_count_a = 0
# vowel_count_e = 0
# vowel_count_i = 0
# vowel_count_o = 0
# vowel_count_u = 0

# Counts the number of vowels in the inputted string.
user_input = str.lower(input("Please enter a string: "))
for i in range(len(user_input)):
    if user_input[i] in vowel_list:
        
        # Counts the sum of each vowels found in the inputted string.
        if user_input[i] == "a":
            vowel_count_found[user_input[i]] += 1 # Is there a way to add to a non-string key value in dict?
            vowel_count += 1
        elif user_input[i] == "e":
            vowel_count_found[user_input[i]] += 1
            vowel_count += 1
        elif user_input[i] == "i":
            vowel_count_found[user_input[i]] += 1
            vowel_count += 1
        elif user_input[i] == "o":
            vowel_count_found[user_input[i]] += 1
            vowel_count += 1
        elif user_input[i] == "u":
            vowel_count_found[user_input[i]] += 1
            vowel_count += 1


# Prints out how much vowels are in the string based on certain conditions.
if vowel_count == 0:
    print("There are no vowels.")
elif vowel_count == 1:
    print("There is only one vowel.")
else:
    print(f"There are {vowel_count} vowels.")

# Prints out the sum of each vowels found in the inputted string.
for i, j in vowel_count_found.items():
    print(i + ":" + str(j))

# For design/spacing.    
print("") 
   
