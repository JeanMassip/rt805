from questions.sign import sign_question
from questions.activity.creation import home_question
from scenarios.sign import sign_in, sign_up, sign_out
from scenarios.activity.creation.creation import creation
from scenarios.activity.modification.modification import modification

#Set a user id
session = dict()
session['user_id'] = 5

# Firt form log or reg
# answer = sign_question()

# # Login / Register
# if answer == "Sign in":
#     sign_in()
# else:
#     sign_up()

print("Welcome to Barathon app!")

# Launch / visit / exit
barathon = True
while barathon:
    
    #Activity - home page
    answer = home_question()

    if answer == "Start a new activity":
        creation(session)
    elif answer == "Visit activities":
        modification(session)
    else:
        print('See you next time!')
        barathon = False

sign_out()

