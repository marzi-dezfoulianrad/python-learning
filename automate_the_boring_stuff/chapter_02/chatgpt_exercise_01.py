# Guessing the number game

import random

startingPoint = input("Hey! Wanna play a guessing game? (yes/no): ").strip().lower()

if startingPoint == 'yes':
    print("Great! Let's start! The number is between 1 and 10.")
    print("You have 3 attempts to guess the number.")
else:
    print("Okay, maybe next time!")
    exit()

randomNumber = random.randint(1, 10)

firstAttempt = 0

while firstAttempt < 3:
    guess = int(input("Enter your guess: "))
    if guess == randomNumber:
        print("Correct!")
        break
    else:
        firstAttempt += 1
        if guess < randomNumber:
            print("Too low!")
        elif guess > randomNumber:
            print("Too high!")
else:
    print("Sorry, you're out of attempts.")
