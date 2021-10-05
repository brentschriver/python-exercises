# 1. Conditional Basics
#   a. prompt the user for a day of the week, print out whether the day is Monday or not
#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
#   c. create variables and make up values for
#       * the number of hours worked in one week
#       * the hourly rate
#       * how much the week's paycheck will be
#       write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours


# 1.a
day_of_the_week = input('What is the day today? ')
if day_of_the_week.lower() == 'monday' or day_of_the_week == 'mon':
    print('The day is Monday.')
else:
    print('The day is not Monday.')

# 1.b
is_weekend = input('What is the day today? ')
if is_weekend.lower() == 'saturday' or is_weekend.lower == 'sunday':
    print('Today is a weekend')
else: 
    print('Today is a weekday')

# 1.c
number_of_hours_worked = 32
overtime = number_of_hours_worked - 40
hourly_rate = 15
if number_of_hours_worked > 40:
    weeks_pay = (number_of_hours_worked * hourly_rate) + (overtime * (15 * 1.5))
else:
    weeks_pay = (number_of_hours_worked * hourly_rate)

print(weeks_pay)


# 2. Loop Basics
#   a. While
#       * Create an integer variable i with a value of 5.
#       * Create a while loop that runs so long as i is less than or equal to 15.
#       * Each loop iteration, output the current value of i, then increment i by one.

# 2.a
i = 5
while i <= 15:
    print(i)
    i += 1

#       * Create a while loop that will count by 2's starting with 0 and ending at 100.
i = 0
while i <= 100:
    print(i)
    i += 2

#       * Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

#       * Create a while loop that starts at 2 and displays the number squared on each line while the number is less than 1,000,000.

i = 2
while i < 1000000:
    print(i)
    i = i ** 2

i = 100
while i >= 5:
    print(i)
    i -= 5


# 2.b.i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number

i = 1
user_number = int(input('Please input a number:'))
while i <= 10:
    print(user_number, 'x', i, '=', user_number * i)
    i += 1


# 2.b.ii

i = 1
while i < 10:
    print(str(i) * i)
    i += 1


# 2.c Break and Continue

# This WHILE loop will continue until the IF conditions are met
while True:
    user_input = input('Please choose a positive, odd number between 1-50:')
    if user_input.isdigit() == True and int(user_input) % 2 != 0 and int(user_input) >= 1 and int(user_input) < 50:
        break
# After the WHILE loop breaks this FOR loop will run
for n in range(50):
    # If the current number is even the program will ignore and continue
    if n % 2 == 0:
        continue
    else:
        if n == int(user_input):
            print('Yikes! Skipping this number:', n)
        else:
            print(f'Here is an odd number: {n}')
   


# 2.d
'''The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a 
loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function 
returns a string, so you'll need to convert this to a numeric type.'''

while True:
    user_i = input('Please input a positive number:')
    if user_i.isdigit() == True and int(user_i) > 0:
        break
for n in range(int(user_i) + 1):
    print(n)


# 2.e

while True:
    user_input = input('Please input a positive number:')
    if user_input.isdigit() == True and int(user_input) > 0:
        break
for n in range(0, int(user_input)):
    print(int(user_input))
    user_input = int(user_input) - 1
    if int(user_input) < 1:
        break


# 3. Fizzbuzz
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)


# 4. Display a table of powers.

user_input = input('What number would you like to go to: ')
print('Here is your table!')
print('number   |   squared  |  cubed   ')
print('_________________________________')

for n in range(1, int(user_input)):
    print(n,'      |',n ** 2,'      |', n ** 3)


# 5. Convert given number grades into letter grades.


while True:
    grade = input('Please input the student\'s grade: ')
    if int(grade) <= 59:
        print('Student grade: F')
    elif int(grade) <= 66:
        print('Student grade: D')
    elif int(grade) <= 79:
        print('Student grade: C')
    elif int(grade) <= 87:
        print('Student grade: B')
    else:
        print('Student grade: A')
    more = input('Would you like to input another grade? (Y/N)')
    if more.lower() == 'n':
        break


# 6. Create a list of dictionaries where each dictionary contains a book that you have read. Each dictionary should have the keys
# 'title', 'author', and 'genre'. Loop through the list and print out information about each book.

the_books_that_i_have_read = [
    {'title': 'The Wind Up Bird Chronicle', 'author': 'Haruki Murakami', 'genre': 'Surrealism'},
    {'title': 'The 13 1/2 Lives of Captain Bluebear', 'author': 'Walter Moers', 'genre': 'Fantasy'},
    {'title': 'White Teeth', 'author': 'Zadie Smith', 'genre': 'Drama'},
    {'title': 'The City of Dreaming Books', 'author': 'Walter Moers', 'genre': 'Fantasy'},
    {'title': '1Q84', 'author': 'Haruki Murakami', 'genre': 'Surrealism'},
    {'title': 'Norwegian Wood', 'author': 'Haruki Murakami', 'genre': 'Surrealism'},
    {'title': 'Colorless Tsukuru Tazaki and his Years of Pilgrimage', 'author': 'Haruki Murakami', 'genre': 'Surrealism'},
    {'title': 'Kafka on the Shore', 'author': 'Haruki Murakami', 'genre': 'Surrealism'},
    {'title': 'Men Without Women', 'author': 'Haruki Murakami', 'genre': 'Short Stories'},
    {'title': 'Rumo and His Miraculous Adventures', 'author': 'Walter Moers', 'genre': 'Fantasy'},
    {'title': 'The Origin of Species', 'author': 'Charles Darwin', 'genre': 'Science Literature'},
    {'title': 'Elementary Korean', 'author': 'Ross King & Jaehoon Yeon', 'genre': 'Language'},
]

user_input = input('Please choose a genre: ')
for book in the_books_that_i_have_read:
    if book['genre'] == user_input:
        print(book['title'])
           


