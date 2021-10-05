# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)


# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]


# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)



# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def has_vowels(string):
    vowel_count = 0
    for letter in string:
        if "a" in letter or "e" in letter or "i" in letter or "o" in letter or "u" in letter:
            vowel_count += 1
    return vowel_count

fruits_with_more_than_two_vowels = [has_vowels(fruit) > 2 for fruit in fruits]
print(fruits_with_more_than_two_vowels)


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = []
for fruit in fruits:
    if has_vowels(fruit) == 2:
        fruits_with_only_two_vowels.append(fruit)



# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_characters = []

for fruit in fruits:
    if len(fruit) > 5:
        fruits_with_more_than_five_characters.append(fruit)
    


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_five_characters = []

for fruit in fruits:
    if len(fruit) == 5:
        fruits_with_exactly_five_characters.append(fruit)


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_characters = []

for fruit in fruits:
    if len(fruit) < 5:
        fruits_with_less_than_five_characters.append(fruit)


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
number_of_characters_in_the_fruit = []

for fruit in fruits:
    number_of_characters_in_the_fruit.append(len(fruit))


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = []

for fruit in fruits:
    if 'a' in fruit:
        fruits_with_letter_a.append(fruit)



# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)



# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = []

for number in numbers:
    if number % 2 !=0:
        odd_numbers.append(number)



# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = []

for number in numbers:
    if number >= 0:
        positive_numbers.append(number)



# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = []

for number in numbers:
    if number < 0:
        negative_numbers.append(number)



# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numbers_with_two_or_more_numerals = []

for number in numbers:
    if len(str(abs(number))) > 1:
        numbers_with_two_or_more_numerals.append(number)



# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = []

for number in numbers:
    numbers_squared.append(number ** 2)



# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = []

for number in numbers:
    if number < 0 and number % 2 !=0:
        odd_negative_numbers.append(number)



# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = []

for number in numbers:
    numbers_plus_5.append(number + 5)



# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime(number):
    if number <= 0:
        return False
    else:
        dividers = [r for r in range(2, number)]
        return len([divider for divider in dividers if number % divider == 0]) == 0
