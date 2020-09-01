# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Use a breakpoint in the code line below to debug your script.
# Press the green button in the gutter to run the script.
from random import randint  # imports a random number randint, which can be used with variables
print("Welcome")
secret = randint(1, 10)
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You Win!")
    else:
        if guess > secret:
            print("Too High!")
        else:
            print("Too Low!")
print("Game Over!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
