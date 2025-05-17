name = ''
while name != 'Joe':
    name = input('Who are you? ')


password = ''
while password != 'swordfish':
    print(f'Hello, {name}. What is the password?')
    password = input()

print('Access granted')
