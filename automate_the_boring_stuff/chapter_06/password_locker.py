"""
#! python3
# password_locker.py - An insecure password locker program.


PASSWORDS = {
    'email': 'F7MINM567hjakb9656aojoKADKOdkn',
    'blog': 'aljljclk6464joijLKAKSN',
    'luggage': '12345'
}

#import sys
#if len(sys.argv) < 2:
#    print('Using: python password_clocker [account] - copy account password')
#    sys.exit()

#account = sys.argv[1]

import sys,pyperclip
if len(sys.argv) < 2:
    print('Using: py oassword_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + 'copied to clipboard.')
else:
    print('There is no account named' + account)
"""

# The part above was all from the book, now i wanna make it more interactive:
#! python3

import sys
import pyperclip

PASSWORDS = {
    'email': 'F7MINM567hjakb9656aojoKADKOdkn',
    'blog': 'aljljclk6464joijLKAKSN',
    'luggage': '12345'
}

def get_password():
    print("Password Locker")
    print("***************")
    while True:
        account_name = input("Enter the account name or type 'List' to see accounts, also 'exit' to quit ;)  ").strip().lower()

        if account_name == 'exit':
            print("You are leaving password locker.")
            sys.exit()

        elif account_name == 'list':
            if PASSWORDS:
                print("\n The Available Accounts are:")
                for acc in PASSWORDS.keys():
                    print(f"-{acc}")
                print("-" * 20)
            else:
                print("NO ACC IS STORED!")

        elif account_name in PASSWORDS:
            pyperclip.copy(PASSWORDS[account_name])
            print(f"Password for '{account_name}' copied to clipboard.")
            break
        else:
            print(f"Error! No {account_name} was found!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        account_from_cmd = sys.argv[1].strip().lower()

        if  account_from_cmd in PASSWORDS:
            pyperclip.copy(PASSWORDS[account_from_cmd])
            print(f"Password for {account_from_cmd} is copied.")
            sys.exit()
        else:
            print(f"Error! No acc was found!")
            choice = input("Would you like to enter the interactive mode? (yes/no): ").strip().lower()
            if choice == 'yes':
                get_password()
            elif choice == 'no':
                sys.exit()
            


get_password()
