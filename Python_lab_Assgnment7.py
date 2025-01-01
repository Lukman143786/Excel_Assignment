1. Print the table of 5 using for loop


Solution:

	for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


Output:
	5 x 1 = 5
	5 x 2 = 10


2.     Print even number series by taking input from the user:

Solution:
	num = int(input("Enter a number: "))

	# Printing even numbers up to the given number
	print("Even numbers:")
	for i in range(2, num + 1, 2)
    	print(i)

Output:
	Enter a number: 10
	Even numbers:
	2
	4
	6
	8
	10


3.     Create a list and iterate through its items using a for loop:


Solution:

# Creating a list
my_list = [10, 20, 30, 40, 50]

# Iterating through the list
print("List items:")
for item in my_list:
    print(item)


Output:
List items:
10
20
30
40
50



4.     Calculate the sum of numbers from 1 to 10 


Solution:

# Calculating the sum using a for loop
total = 0
for i in range(1, 11):
    total += i

# Displaying the sum
print(f"The sum of numbers from 1 to 10 is {total}.")


Output:
The sum of numbers from 1 to 10 is 55.


5. print the pattern   



Solution:

# Printing the pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


Output:

   	   *
         ***
       *****
      *******
     *********


6. Print the first 10 natural numbers using for loop 



Solution:


# Printing the first 10 natural numbers
print("The first 10 natural numbers:")
for i in range(1, 11):
    print(i)


Output:


The first 10 natural numbers:
1
2
...
10


7. Python program to check if the given string is a palindrome 


Solution:


# Taking input from the user
text = input("Enter a string: ")

# Checking if the string is a palindrome
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


Output:
Enter a string: madam
The string is a palindrome.


8. Python program to check if a given number is an Armstrong number


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



 9. Python program to get the Fibonacci series between 0 to 50 


Solution:

# Printing Fibonacci series between 0 to 50
a, b = 0, 1
print("Fibonacci series:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b



Output:

Fibonacci series:
0 1 1 2 3 5 8 13 21 34


10. Python program to check the validity of password input by users



Solution:

# Taking password input from the user
password = input("Enter your password: ")

# Checking validity of the password
if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password):
    print("Valid password.")
else:
    print("Invalid password.")


Output:

Enter your password: Pass1234
Valid password.
