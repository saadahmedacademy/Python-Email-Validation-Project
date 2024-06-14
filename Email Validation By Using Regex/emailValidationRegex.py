# Email Validation By Using RegEx
from typing import Union
import re

email_conditions = r"^[a-z]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter Your Email For Validation: ") 

if re.search(email_conditions,user_email):
    print("Right Email")
else:
    print(f'''
    Something went wrong in your email {user_email},
    please follow the below conditions.

    1 First letter of email should alphabetic,
    2 Dont use "_" or "." two times in your email.
    3 Use @ and . in your email.
    4 "." must be after @ and before at least last 2 digits.
    ''')              