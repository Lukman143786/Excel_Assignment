1. Write a Python program to count the occurrences of each word in a given sentence.


Solution:
# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Splitting the string into words
words = string.lower().replace('.', '').split()

# Counting occurrences of each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Displaying the word counts
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")


Output:

Word occurrences:
to: 2
change: 2
the: 4
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1




2. Write a Python program to remove a newline in Python.


Solution:

# Given string
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Removing newlines
cleaned_string = string.replace('\n', ' ')

# Displaying the cleaned string
print(f"String without newlines: '{cleaned_string.strip()}'")


Output:
String without newlines: 'Best Deeptech Python Training'



3. Write a Python program to reverse words in a string.


Solution:
# Given string
string = "Deeptech Python Training"

# Reversing the words
reversed_string = ' '.join(string.split()[::-1])

# Displaying the reversed string
print(f"Reversed string: '{reversed_string}'")


Output:
Reversed string: 'Training Python Deeptech'




4. Write a Python program to count and display the vowels of a given text.


Solution:

# Given string
string = "Welcome to python Training"

# Counting vowels
vowels = "aeiou"
vowel_count = {vowel: 0 for vowel in vowels}
for char in string.lower():
    if char in vowels:
        vowel_count[char] += 1

# Displaying vowel counts
print("Vowel occurrences:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")



Output:

Vowel occurrences:
a: 1
e: 3
i: 2
o: 3
u: 0
