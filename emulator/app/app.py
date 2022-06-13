#!/bin/python3.8

# from questions.home import home_question
from questions.questions import *
from scenarios.sign import sign_in, sign_up, sign_out

# Home
answer = home_question()

# Login / Register
if answer == "Sign in":
    sign_in()
else:
    sign_up()

print("Welcome to Barathon app!")

# Activity - home page
answer = activity_question()

# Launch / visit / exit
barathon = True
while barathon:
    if answer == "Start a new activity":
        new_activity()
    elif answer == "Visit activities":
        print("visit")
    else:
        print('See you next time!')
        barathon = False

sign_out()

