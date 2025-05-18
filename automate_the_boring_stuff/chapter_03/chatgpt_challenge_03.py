# Password Strength Checker
# A strong password must: Be at least 8 characters long. Contain both uppercase and lowercase letters. Include at least one digit.

print("Password Strength Checker")
password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

if has_upper and has_lower and has_digit and len(password) >= 8:
    print("Password is strong.")
else:
    print("Password is weak.")