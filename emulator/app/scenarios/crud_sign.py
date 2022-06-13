#!/bin/python3.8

from functions.validation import login_validation, password_validation
from functions.xml_building import build_signin_xml
from functions.request_building import send_post_request
from functions.request_building import send_post_request
from questions.user_credentials import user_credentials

def sign_in():
    #Get input login & password from user with valdiation
    answers = user_credentials()
       
    #Build XML -> return none type that could print out
    # xml_data = build_signin_xml(answers['login'], answers['password'])

    #Send XML to web server over the network
    # send_post_request(xml_data)

def sign_up():
    #Get input logi & password from user with validation
    answers = user_credentials()

    #Build XML -> return none type that could print out
    # xml_data = build_signup_xml(answers['login'], answers['password'])

    #Send XML to web server over the network
    # send_post_request(xml_data)

def sign_out():
    url="api/sign-out"
    send_post_request(url)