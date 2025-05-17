# This program says hello and asks for name and age.

print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, '+ myName)
print('The lenght of your name is: ', len(myName))
print('What is your age?')
myAge= input()
print('You will be ' + str(int(myAge) + 1) + ' Min a year.')