from password_generator import PasswordGenerator as pg

class GenerateTweet():
    """Class for generating a tweet that contains the generated password."""
    
    def __init__(self):
        """Initialize the generated tweet object."""
        self.generated_password = pg()
        self.string = f"The password of the day is:\n{self.generated_password.password}"
        
    def print_(self):
        """Print method, for printing out the class variables. Used for testing."""
        print(self.string)