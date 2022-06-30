from functions.create_dict import dict_sign_in, dict_sign_up
from functions.end_point_requests import sign_in_request, sign_up_request, sign_out_request
from questions.sign import user_credentials

def sign_in():
    #Get input login & password from user with valdiation
    answers = user_credentials()
       
    #Create a dict format
    payload = dict_sign_in(answers['login'], answers['password'])

    #Send dict to web server over the network
    sign_in_request(payload)

def sign_up():
    #Get input login & password from user with validation
    answers = user_credentials()

    #Create a dict format
    payload = dict_sign_up(answers['login'], answers['password'])

    #Send dict to web server over the network
    sign_up_request(payload)

def sign_out():
    sign_out_request()