"""
https://developer.twitter.com/en/docs/platform-overview
Note to develpoper: Use the twitter API to improve this project.
"""

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from generate_tweet import GenerateTweet as gt

email_input_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
next_button = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]"
password_input_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
login_button_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div"
text_field_xpath = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
post_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'

class Main():
    """Main class meant to implement the PasswordGenerator and GenerateTweet classes."""
    
    def __init__(self):
        self.username, self.password = self._retrieve_username_password()
        self.generated_tweet = gt()
        self.tweet = self.generated_tweet.string
    
    def print_(self):
        """Print method, for printing out the class variables. Used for testing."""
        print(self.username, self.password, self.tweet)

    def _retrieve_username_password(self):
        """Method used to retrieve twitter username and password from a text file, located in the parent directory."""
        with open(r'C:\Users\usr\Desktop\OFFICE\Macibas_projekti\Web\password_twitter_bot_generate_password.txt') as file_object:
            login_info = file_object.read().split('\n')
            file_object.close()
            username = login_info[0]
            password = login_info[1]
            return username, password
    
    def send_tweet(self):
        """Method used to do the appropriate autonmation and send the tweet."""
        self._automation_setup()
        
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.get('https://twitter.com/i/flow/login')
        
        time.sleep(5)
        driver.find_element("xpath", email_input_xpath).send_keys(self.username)
        time.sleep(0.5)
        driver.find_element("xpath", next_button).click()
        time.sleep(0.5)
        driver.find_element("xpath", password_input_xpath).send_keys(self.password)
        time.sleep(1)
        driver.find_element("xpath", login_button_xpath).click()
        time.sleep(10)
        driver.find_element("xpath", text_field_xpath).send_keys(self.tweet)
        time.sleep(0.5)
        driver.find_element("xpath", post_button_xpath).click()
        time.sleep(0.5)
        driver.close()
    
    def _automation_setup(self):
        """Helper method used to set up the automation process."""
        # display = Display(visible=0, size=(800, 600))
        # display.start()
        options = Options()
        options.add_argument("start-maximized")
     
if __name__ == '__main__':   
    try:
        print("#######Try?catch block has started#######\n")
        main = Main()
        main.send_tweet()
    finally:
        print("\n#######Try/Catch block has finished succesfully#######")