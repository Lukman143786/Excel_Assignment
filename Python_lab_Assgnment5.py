{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4a87aec9-83f0-4708-88be-594020a64fea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The division result is 5.0.\n"
     ]
    }
   ],
   "source": [
    "# Defining the function\n",
    "def div(a, b):\n",
    "    return a / b\n",
    "\n",
    "# Calling the function with two numbers\n",
    "result = div(10, 2)\n",
    "\n",
    "print(f\"The division result is {result}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b817dbfc-3385-4c4b-855d-fe918af51294",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The square of the number is 16.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def square(x):\n",
    "    return x ** 2\n",
    "\n",
    "# Calling the function with a number\n",
    "result = square(4)\n",
    "\n",
    "# Displaying the square\n",
    "print(f\"The square of the number is {result}.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5b6ad695-71c7-482e-a898-0de92acefff5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The random numbers are: [21, 81, 71, 72, 2]\n",
      "The maximum number is 81.\n",
      "The minimum number is 2.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# Generating 5 random numbers\n",
    "numbers = [random.randint(1, 100) for _ in range(5)]\n",
    "\n",
    "# Finding the maximum and minimum\n",
    "maximum = max(numbers)\n",
    "minimum = min(numbers)\n",
    "\n",
    "# Displaying the numbers, maximum, and minimum\n",
    "print(f\"The random numbers are: {numbers}\")\n",
    "print(f\"The maximum number is {maximum}.\")\n",
    "print(f\"The minimum number is {minimum}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5b1397a2-41b9-49ce-beda-61478580eda6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your name:  Lukman\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your name in lowercase is lukman.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Accepting a name from the user\n",
    "name = input(\"Enter your name: \")\n",
    "\n",
    "# Displaying the name in lowercase\n",
    "print(f\"Your name in lowercase is {name.lower()}.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
