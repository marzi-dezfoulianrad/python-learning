# Importing time
import time 

# GETTING THE USER INPUT AND TURNING IT INTO INT
userInput = int(input('Hey! Give me a number bigger than 3! I will provide some infos:'))

# CHECKING IF ITS REALLY BIGGER OR THE USER IS PRANKING US :D
def biggerThanThree(number):
    time.sleep(2)
    if number > 3:
        print('Well, your number is obviously bigger than 3.')
    elif number < 3 and number >= 0:
        print ('BRUH! PLEASE WRITE A NUMBER BIGGER THAN 3! BITTE!')
    elif number == 3:
        print('A THREE????')

# Checking if the number is negative 
def ifItsNegative(number):
    time.sleep(2)
    if number < 0:
        print('Hmmm... a negative number? You might be smart after all.')

# CHECKING IF ITS ODD OR EVEN
def oddOrEven(number):
    time.sleep(2)
    if number <= 3 and number >= 0:
        print(f'Really? {number}? You are smarter than that!')
    elif not number % 2 and number > 0:
        print('Your number is even, right? :D')
    elif number % 2 and number > 0:
        print('Your name is an odd number, ja?')

# Writing the number before that number
def numbersBefore(number):  
    if number <= 3 and number > 0:  
        print('Your number is simply just too simple!')  
    elif number > 3 and number > 0:  
        if number % 2 == 0:  
            print(f'Before we get to your number, {number}, here are the even numbers that came before it:')  
            for i in range(2, number + 1, 2):  
                print(i, end=" ")  
        else:  
            print(f'Before we get to your number, {number}, here are the odd numbers that came before it:')  
            for i in range(1, number + 1, 2):  
                print(i, end=" ")  

biggerThanThree(userInput)
ifItsNegative(userInput)
oddOrEven(userInput)
numbersBefore(userInput)
