from random import *

# generate a random number between 1 and 101
randNum = randint(1, 101)

# function for outputing whether the guess is correct, too high, or too low
# according to the guess
def guess(num):
    if num > randNum:
        print("[{}] Too high, try again!\n".format(num))
    elif num < randNum:
        print("[{}] Too low, try again!\n".format(num))
    else:
        print("[{}] Correct. You win!\n".format(num))

# while loop for running until the correct answer is given by input
while(True):
    num = int(input("What's your guess? "))
    guess(num)
    if num == randNum:
        break