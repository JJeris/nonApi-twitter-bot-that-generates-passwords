###### Imported libraries, script files

## Sys import
import sys
sys.path.append(".")
## Sys import


## Custom script import
# print(password_gen.generate_password())
# from generate_password_script.password_gen import *
# from generate_password_script import *
import generate_password_script.password_generator as passgen
import generate_tweet_script.generate_tweet as tweetgen
## Custom script import


## Selenium import
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from pyvirtualdisplay import Display
## Selenium import


## Time import
import time
## Time import


'''
Notes to developer
https://www.youtube.com/watch?v=9wC5mFkcqqg&ab_channel=CreepyD
A good video that shows how to automate using Selenium
DONE!!!!!!


Need:
-How to shcedule it
-How to run it in the background
-Rework the bot and make a V2.0 after this (PEP8), V1.0 is finished.

Further plans:
-make a trading bot using schedule, evaluation and Selenium. Good luck :D
'''
### Constants
email_input_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
next_button = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]"
password_input_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
login_button = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div"
text_field = "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div"
post = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'



### Functions section
def retrieve_username_password():
    """
    The path to this .txt file should be defined by the user himself. It cotains the twitter username (1st line) and the accounts password (2nd) line.
    The username and password are stored in a txt file which is outisde of the projects scope, so as to ensure that the login info cannot be viewed on github.
    """
    f = open(r'C:\Users\usr\Desktop\OFFICE\Macibas_projekti\Web\password_twitter_bot_generate_password.txt', 'r')
    login_info = f.read().split("\n")
    f.close()
    username = login_info[0]
    password = login_info[1]
    return username, password


### Demo
try:
    
    ### Retrieving data 
    print("#######Try?catch block has started#######\n")
    username, login_password = retrieve_username_password()
    
    tweet = tweetgen.generate_tweet(password = passgen.generate_password())
    
    ### Automation 
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    options = Options()
    options.add_argument("start-maximized")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.get('https://twitter.com/i/flow/login')
    
    ### Execution
    # Add waiters, that wait till the pages have loaded. Otherwise the code will fail.
    time.sleep(5)
    driver.find_element("xpath", email_input_xpath).send_keys(username)
    time.sleep(0.5)
    driver.find_element("xpath", next_button).click()
    time.sleep(0.5)
    driver.find_element("xpath", password_input_xpath).send_keys(login_password)
    time.sleep(1)
    driver.find_element("xpath", login_button).click()
    time.sleep(10)
    driver.find_element("xpath", text_field).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element("xpath", post).click()
    time.sleep(0.5)
    driver.close()
finally:
    print("\n#######Try/Catch block has finished succesfully#######")
  
