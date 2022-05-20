#!/bin/python3.8

from questions.home import home_question
from scenarios.crud_sign import sign_in

# Home
answer = home_question()

# Login / Register
if answer == "Sign in":
    sign_in()
else:
    sign_up()