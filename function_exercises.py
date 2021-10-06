# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2:
        return True
    else:
        return False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(vowel):
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or vowel == 'U':
        return True
    else:
        return False
    
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(vowel):
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or vowel == 'U':
        return False
    else:
        return True
    
print(is_consonant('a'))

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_word(word):
    splitstring = word.split()
    if word[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return word
    else:
        return word.capitalize()

print(capitalize_word('embEBers'))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip, bill_total):
    amount_to_tip = tip * bill_total
    return amount_to_tip


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    new_price = original_price * (1 - discount_percentage)
    return new_price

print(apply_discount(100, .33))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(string_with_commas):
    no_commas = int(string_with_commas.replace(',',''))
  
    return no_commas

print(handle_commas('1,324,234'))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
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

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(anyword): 
    new_word = ''
    for letter in anyword:   
        if is_vowel(letter) == True:
            new_word = new_word.replace(letter, '')
        elif is_vowel(letter) == False:
            new_word = new_word + letter
    return new_word

vowel = ['a','e','i','o','u','A','E','I','O','U']

'''10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed '''

def normalize_name(string):
    for char in string:
        if (char.isalnum() == False
            and char != ' '):
            string = string.replace(char,'')
    string = string.lower().strip()
    string = string.replace(' ', '_')
    return string



# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

def cumulative_sum(array):
    curr_position_in_array = 0
    cumulative_sum = 0
    length_of_array = len(array)
    cumulative_sum_list = []
    while curr_position_in_array < length_of_array:
        for n in array:
            cumulative_sum_list.append(cumulative_sum + n)
            cumulative_sum += n
            curr_position_in_array += 1
    return cumulative_sum_list
    

print(cumulative_sum([1,1,1]))

