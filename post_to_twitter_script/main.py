### Imported libraries, script files
import sys
sys.path.append(".")
# print(password_gen.generate_password())
# from generate_password_script.password_gen import *
# from generate_password_script import *
import generate_password_script.password_generator as passgen
import generate_tweet_script.generate_tweet as tweetgen

'''
https://www.youtube.com/watch?v=9wC5mFkcqqg&ab_channel=CreepyD
A good video that shows how to automate using Selenium

Need:
-How to shcedule it
-How to run it in the background
-Rework the bot and make a V2.0 after this, V1.0 is finished.

Further plans:
-make a trading bot using schedule, evaluation and Selenium. Good luck :D
'''

### Functions section
def retrieve_username_password():
    """
    The path to this .txt file should be defined by the user himself. It cotains the twitter username (1st line) and the accounts password (2nd) line.
    
    The username and password are stored in a txt file which is outisde of the projects scope, so as to ensure that the login info cannot be viewed on github.
    """
    f = open(r'C:\Users\usr\Desktop\OFFICE\Macibas_projekti\Web\password_twitter_bot_generate_password.txt', 'r')
    login_info = f.read().split("\n")
    f.close()
    return login_info



### Integration section


### Demo section
try:
    print()
    login_arr = retrieve_username_password()
    print(login_arr)
    password = passgen.generate_password()
    print(password)
    tweet = tweetgen.generate_tweet(password)
    print(tweet)
finally:
    print("\n#######Try/Catch block has finished succesfully#######")
  
