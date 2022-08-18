"""
password_gen.py
Made by JJeris

About:

Programs purpose is to create a random password (a string of characters that consist of 
letters, both uppercase and lowercase, numbers and symbols). The passwords are gibberish
which means theyll be even harder to crack and or guess by malicious parties.

-JJeris

"""

"""
Used libraries
"""

import random
"""
Assets - lists of characters that will be used in the generation of a password.
"""
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
SYMBOLS = "`~!@#$%^&*()_+-={|[]\:;<>?,./:"




"""

"""
def generate_length():
    length = random.randint(20, 253)
    return length





"""
add_length()

Aboutme:
This function takes a user input for the length of the password, 
which he wishes to generate.

In addition to that, it also validates that the given length is not equal or less than 0.

"""
def add_length(length):
    if length <= 0 or length > 252:
        # raise Exception("THROWN ERROR: Entered number cannot be less or equal to ZERO.")
        raise TypeError("Length cannot be less or equal to 0 or more than 252")
    # while length <= 0:
        # print("Input invalid")
        # NEEDS TO THROW AN ERROR
        # length = int(input(">Input "))
    return length
    


"""
generate_password()

Aboutme:
This function generates the password, which will be as long as the user given input
in the Add_length() function.

The password is generated using the random module for Python. It chooses a number from 1-5,
which determins which one of the globally declared lists will be used (the numbers
corresponding to the list in the order that they were declared).

Then, finding out which list is to be used for the next character in the password, another 
random number is chosen in the borders of 1-length_of_the_given_list. The password string variable
gets appended with the character, whose index in the given list equals the randomly chosen number.

"""
def generate_password():
    length = generate_length()
    password_length = add_length(length)
    password_output = ""
    for i in range(0, password_length):
        x = random.randrange (1, 5)
        if x==1:
            x1 = random.randrange(len(UPPERCASE_LETTERS))
            password_output += UPPERCASE_LETTERS[x1]
        elif x==2:
            x2 = random.randrange(len(LOWERCASE_LETTERS))
            password_output += LOWERCASE_LETTERS[x2]
        elif x==3:
            x3 = random.randrange(len(NUMBERS))
            password_output += NUMBERS[x3] 
        elif x==4:
            x4 = random.randrange(len(SYMBOLS))
            password_output += SYMBOLS[x4]
    return password_output

"""
To test this code, simply comment out the next line.
"""
# generate_length()