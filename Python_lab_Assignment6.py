1. Write a Python program to reverse a number using a while loop.
Solution:

# Taking input from the user
num = int(input("Enter a number: "))
reversed_num = 0

# Reversing the number using a while loop
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Displaying the reversed number
print(f"The reversed number is {reversed_num}.")


Output:
Enter a number: 1234
The reversed number is 4321.


2. Write a Python program to check whether a number is palindrome or not.
Solution:

# Taking input from the user
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

# Reversing the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Checking if the number is a palindrome
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


Output:
Enter a number: 121
The number is a palindrome.


3. Write a Python program to find the factorial of a given number using a while loop.



Solution:

# Taking input from the user
num = int(input("Enter a number: "))
factorial = 1

# Calculating factorial using a while loop
while num > 0:
    factorial *= num
    num -= 1

# Displaying the factorial
print(f"The factorial is {factorial}.")


Output:

Enter a number: 5
The factorial is 120.



4. Accept numbers using input() function until the user enters 0. If user inputs 0, break the while loop and display the sum of all the numbers.


Solution:

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

# Displaying the sum of the numbers
print(f"The sum of all the numbers is {total}.")


Output:
Enter a number (0 to stop): 5
Enter a number (0 to stop): 10
Enter a number (0 to stop): 0
The sum of all the numbers is 15.



1. Program to check whether the given number is palindrome or not.


Solution:

# Taking input from the user
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

# Reversing the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Checking if the number is a palindrome
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

Output:
Enter a number: 121
The number is a palindrome.


2. Program to check whether the given number is Armstrong or not.


Solution:

# Taking input from the user
num = int(input("Enter a number: "))
original_num = num
sum_of_cubes = 0

# Checking if the number is an Armstrong number
while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num //= 10

if original_num == sum_of_cubes:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")


Output:
Enter a number: 153
The number is an Armstrong number.



3. Program to find the factorial of a number.


Solution:
# Taking input from the user
num = int(input("Enter a number: "))
factorial = 1

# Calculating factorial using a while loop
while num > 0:
    factorial *= num
    num -= 1

# Displaying the factorial
print(f"The factorial is {factorial}.")


Output:
Enter a number: 5
The factorial is 120.