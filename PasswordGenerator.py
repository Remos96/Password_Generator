import random

print("This password generator contains all uppercase and lower case letters, numbers 0-9, and '!@#$%^&*()_+[]|/;<>[]' symbols.")
possible_characters = "adcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]|/;<>[]"
password_size = int(input("Enter the length of characters desired for the password: "))
password_count = int(input("How many passwords should be created: "))

for i in range(password_count):
    password = ""
    for j in range(password_size):
        password_character = random.choice(possible_characters)     # Choose from possible_characters random assortment of letters, allows repeats.
        password += password_character
    print(f"Password {i}: {password}")
