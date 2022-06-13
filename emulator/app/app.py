from questions.sign import sign_question
from questions.activity import home_question
from scenarios.sign import sign_in, sign_up, sign_out
from scenarios.activity import creation
from random import randint

#Set a user id
userId = 5

# Firt form log or reg
answer = sign_question()

# # Login / Register
if answer == "Sign in":
    sign_in()
else:
    sign_up()

print("Welcome to Barathon app!")

# Launch / visit / exit
barathon = True
while barathon:
    
    #Activity - home page
    answer = home_question()

    if answer == "Start a new activity":
        creation(userId)
    elif answer == "Visit activities":
        print("visit")
    else:
        print('See you next time!')
        barathon = False

sign_out()

