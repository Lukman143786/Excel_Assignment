1. Write a Python program to count all letters, digits, and special symbols from the given string.


Solution:

# Given input
input_string = "P@#yn26at^&i5ve"

# Initializing counters
chars, digits, symbols = 0, 0, 0

# Counting each type
for char in input_string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

# Displaying the results
print(f"Chars = {chars} Digits = {digits} Symbols = {symbols}")

Output:
Chars = 8 Digits = 3 Symbols = 4



2. Write a Python program to remove duplicate characters of a given string.
Solution:

# Given input
input_string = "String and String Function"

# Removing duplicate characters while preserving order
result = []
seen = set()
for char in input_string:
    if char not in seen:
        result.append(char)
        seen.add(char)

# Displaying the output
output_string = ''.join(result)
print(f"Output: {output_string}")


Output: String adFuco


3. Write a Python program to count Uppercase, Lowercase, special characters, and numeric values in a given string.


Solution:

# Given input
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initializing counters
uppercase, lowercase, numbers, special = 0, 0, 0, 0

# Counting each type
for char in input_string:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        special += 1

# Displaying the results
print(f"UpperCase: {uppercase} LowerCase: {lowercase} NumberCase: {numbers} SpecialCase: {special}")


Output:
UpperCase: 5 LowerCase: 18 NumberCase: 5 SpecialCase: 11



4. Write a Python program to count vowels in a string.


Solution:

# Given input
input_string = "Welcome to Python Assignment"

# Counting vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)

# Displaying the total number of vowels
print(f"Total vowels are: {vowel_count}")


Output:

Total vowels are: 8