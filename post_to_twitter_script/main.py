### Imported libraries, script files
import sys
sys.path.append(".")
# print(password_gen.generate_password())
# from generate_password_script.password_gen import *
from generate_password_script import *
import generate_password_script.password_generator as passgen




### Integration section
print(passgen.generate_password(10))



### DEMO SECTION
# try:
#   print(passgen.generate_password(0))
# finally: # I don't know why this works, but it does, so... Might need to rework the raising of the error msg in password_generator.py
#     print("Try block finished.")
  
