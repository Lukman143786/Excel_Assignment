1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.


Solution:

number = int(input("Enter a number: "))

# Checking if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

print(f"The number is {result}.")

Output:
Enter a number: 100
The number is Even.


2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
Solution:

age = int(input("Enter your age: "))

# Checking eligibility to vote
result = "Eligible to vote" if age >= 18 else "Not eligible to vote"

print(result)


Output:
Enter your age:  12
Not eligible to vote


3. Write a Python program that determines if a given year is a leap year or not.
Solution:

year = int(input("Enter a year: "))

# Checking if the year is a leap year
result = "Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year"

print(f"{year} is {result}.")


Output:

Enter a year: 2024
2024 is Leap year.



4. Create a Python program that checks if a user-given number is positive, negative, or zero.
Solution:

number = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"

# Printing the result
print(f"The number is {result}.")


Output:
Enter a number: -5
The number is Negative.


5. Write a Python program that determines the largest of three numbers entered by the user.
Solution:


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number
largest = max(num1, num2, num3)

print(f"The largest number is {largest}.")

Output:

Enter the first number: 3
Enter the second number: 9
Enter the third number: 7
The largest number is 9.0.