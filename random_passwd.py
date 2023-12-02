
# This programm help to create Random Password with user input 

# Author : jashkv
# Date   : 1-Dec-2023

import random
import string

def generate_password(length, uppercase_count, lowercase_count, numeric_count, special_count):
    uppercase = ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_count))
    lowercase = ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase_count))
    numbers = ''.join(random.choice(string.digits) for _ in range(numeric_count))
    special = ''.join(random.choice(string.punctuation) for _ in range(special_count))

    all_chars = uppercase + lowercase + numbers + special
    remaining_length = length - (uppercase_count + lowercase_count + numeric_count + special_count)
    all_chars += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))

    password_list = list(all_chars)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

# Get user input for password requirements
length = int(input("Enter password length: "))
uppercase_count = int(input("Enter number of uppercase letters: "))
lowercase_count = int(input("Enter number of lowercase letters: "))
numeric_count = int(input("Enter number of numeric characters: "))
special_count = int(input("Enter number of special characters: "))

# Generate and display the password
password = generate_password(length, uppercase_count, lowercase_count, numeric_count, special_count)
print("\nYour random password is:\n")
print(password)
