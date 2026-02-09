# Write a program that counts up the number of vowels [a, e, i, o,
# u] contained in the string.

# text = input("Enter a string: ")
# vowlels = "aeiouAEIOU"
# count = 0

# for char in text:
#     if char in vowlels:
#         count += 1
# print("Number of vowels:", count)


# Fill an array of 5 elements from the user, Sort it in descending
# and ascending orders then display the output.

# arr = []
# for i in range(5):
#     num = int(input(f"Enter number {i + 1}: "))
#     arr.append(num)

# print("original array:", arr)

# # Ascending order
# arr.sort()
# print("ascending order:", arr)

# # Descending order
# arr.sort(reverse=True)
# print("descending order:", arr)


# Write a program that prints the number of times the string 'iti'
# occurs in anystring.

# text = input("Enter a string: ")
# count = text.count("iti")
# print("Number of occurrences of 'iti':", count)

# ititi


# Write a program that remove all vowels from the input word and
# generate a brief version of it.

# word = input("Enter a word: ")
# vowels = "aeiouAEIOU"
# brief = ""

# for char in word:
#     if char not in vowels:
#         brief += char
# print("Brief version:", brief)


# Write a program that prints the locations of "i" character in any
# string you added.

# text = input("Enter a string: ")

# for i in range(len(text)):
#     if text[i] == 'i':
#         print("i found at index:", i)


# Write a program that generate a multiplication table from 1 to the
# number passed.

# num = int(input("Enter the number to generate the multiplication table: "))

# table = []

# for i in range(1, num + 1):
#     row = []
#     for j in range(1, i + 1):
#         row.append(i * j)
#     table.append(row)

# print(table)

# Write a program that build a Mario pyramid like below:

num = int(input("Enter the length of the pyramid: "))

for i in range(1, num+1):
    row = " " * (num-i)
    row += "*" * i 
    print(row)

