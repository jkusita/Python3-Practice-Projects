# Program that acts like a Magic 8 ball.

import random

while True:
    # Generates a random number so that you can use it to access an element from the reponse_list.
    random_int = random.randint(0, 19)
    # list of different reponses from the Magic 8 ball.
    response_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", " Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My replpy is no.", "My sources say no.", "Outlook not so good.", "Very doubtful"]

    user_input = input("Ask me a yes or no question: ")
    print(response_list[random_int])
    continue_or_exit = input("Type 'c' to continue or 'e' to exit")
    print("\n")
    if continue_or_exit == "e":
        break

        