# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start.

# def generate_array(length, start):
#     arr = []
#     for i in range(length):
#         arr.append(start + i)
#     return arr

# result = generate_array(5, 10)
# print(result)


# write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if is is divisible by both return "FizzBuzz"

# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5  == 0:
#         return "Buzz"
#     else:
#         return num

# print(fizz_buzz(3))  # Fizz
# print(fizz_buzz(5))  # Buzz
# print(fizz_buzz(15)) # FizzBuzz
# print(fizz_buzz(7))  # 7


# Write a function which has an input of a string from user then it
# will return the same string reversed.

# def reverse_string(text):
#     reverse_text = ""
#     for char in text:
#         reverse_text = char + reverse_text
#     return reverse_text

# def reverse_string(text):
#     return text[::-1]

# user_input = input("Enter a string: ")
# result = reverse_string(user_input)
# print("Reversed string:", result)


# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email
# or not

# def is_valid_email(email):
#     if "@" in email and "." in email:
#         at_index = email.index("@")
#         dot_index = email.rindex(".")
#         return (
#             at_index > 0 and 
#             dot_index > at_index + 1 and
#             dot_index < len(email) - 1
#         )
#     return False

# while True:
#     name = input("Enter your name: ").strip()
#     if name and not name.isdigit():
#         break
#     print("Invalid name. Please enter a valid name (not empty or numbers)!")

# while True:
#     email = input("Enter your email: ").strip()
#     if is_valid_email(email):
#         break
#     print("Invalid email. Please enter a valid email address!")


# print("\nUser Data:")
# print("Name:", name)
# print("Email:", email)


# Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu

# def longest_alphabetical_substring(text):
#     longest = ""
#     current = ""

#     for char in text:
#         if current == "" or char >= current[-1]:
#             current += char
#         else:
#             if len(current) > len(longest):
#                 longest = current
#             current = char

#     if len(current) > len(longest):
#         longest = current

#     print("Longest substring in alphabetical order is:", longest)


# longest_alphabetical_substring("abdulrahman")


# Write a program which repeatedly reads numbers until the user
# enters “done”.
# ○ Once “done” is entered, print out the total, count, and
# average of the numbers.
# ○ If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.

# total = 0
# count = 0

# while True:
#     user_input = input("Enter a number (or 'done' to finish): ")
#     if user_input.lower() == "done":
#         break

#     try:
#         num = float(user_input)
#         total += num
#         count += 1
#     except ValueError:
#         print("Invalid input. Please enter a number!")

# if count > 0:
#     average = total / count
# else:
#     average = 0

# print("\nResults:")
# print("Total:", total)
# print("Count:", count)
# print("Average:", average)


# Word guessing game (hangman)
# ○ A list of words will be hardcoded in your program, out of
# which the interpreter will
# ○ choose 1 random word.
# ○ The user first must input their names
# ○ Ask the user to guess any alphabet. If the random word
# contains that alphabet, it
# ○ will be shown as the output(with correct placement)
# ○ Else the program will ask you to guess another alphabet.
# ○ Give 7 turns maximum to guess the complete word.

import random

words = ["python", "hangman", "programming", "computer", "algorithm"]
secret_word = random.choice(words)

while True:
    name = input("Enter your name: ").strip()
    if name and not name.isdigit():
        break
    print("Invalid name! Please enter a valid name.")

print(f"\nHello {name}! Let's play Hangman.")
print(f"The word has {len(secret_word)} letters.")

guessed_word = ["_"] * len(secret_word)
guessed_letters = set()
turns = 7

while turns > 0 and "".join(guessed_word) != secret_word:
    print("\nCurrent word:", " ".join(guessed_word))
    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print(f"Good job! The letter '{guess}' is in the word.")
        for i, char in enumerate(secret_word):
            if char == guess:
                guessed_word[i] = guess
    else:
        turns -= 1
        print(f"Wrong guess! You have {turns} turns left.")


if "".join(guessed_word) == secret_word:
    print(f"\nCongratulations {name}! You guessed the word: {secret_word}")
else:
    print(f"\nGame over! The word was: {secret_word}")
