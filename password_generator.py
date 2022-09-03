import random

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "1234567890"
# SYMBOLS = "`~!$%^&*()_+-={|[]\:;<>?,./:"
SYMBOLS = "`~!$^&*()_+-={|[]:;<>?,./:"

class PasswordGenerator:
    """A class to create a random password."""
    def __init__(self):
        """Initialize the generated password object."""
        self.length = self._generate_length()
        self.password = self._generate_password(self.length)
    
    def print_(self):
        """Print method, for printing out the class variables. Used for testing."""
        print(self.length)
        print(self.password_output)
    
    def _generate_length(self):
        """Helper method to generate the lenght of the password."""
        length = random.randint(20, 253)
        return length
    
    # def _check_length(self, length):
    #     """Helper method used to check, if a user given length is valid."""
    #     print(None)
    #     if length <= 0 or length > 252:
    #         raise TypeError("Length cannot be less or equal to 0 or more than 252 characters.")
    #     return length
    
    def _generate_password(self, length):
        """Helper method to generate the password, using the const strings containing uppercase, lowercase letters, numbers and non alphanumeric symbols."""
        output = ""
        for i in range(0, length):
            character_set_number = random.randrange(1, 5)
            if character_set_number == 1:
                character_set_index = random.randrange(len(UPPERCASE_LETTERS))
                output += UPPERCASE_LETTERS[character_set_index]
            elif character_set_number == 2:
                character_set_index = random.randrange(len(LOWERCASE_LETTERS))
                output += LOWERCASE_LETTERS[character_set_index]
            elif character_set_number == 3:
                character_set_index = random.randrange(len(NUMBERS))
                output += NUMBERS[character_set_index] 
            elif character_set_number == 4:
                character_set_index = random.randrange(len(SYMBOLS))
                output += SYMBOLS[character_set_index]
        return output