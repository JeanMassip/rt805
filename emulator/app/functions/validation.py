import re

def login_validation(user_input):
    valid = False
    pattern="^[a-zA-Z0-9\.\-\_]+@[a-zA-Z]+\.[a-z]{2,4}$"

    if re.search(pattern, user_input):
        valid = True

    return valid

def password_validation(user_input):
    valid = False
    pattern="^[a-zA-Z0-9 \-]{3,20}"

    if re.search(pattern, user_input):
        valid = True
    
    return valid