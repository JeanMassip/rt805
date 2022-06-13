#!/bin/python3.8

from functions.xml_building import *
from functions.request_building import *
from questions.sign import user_credentials

def sign_in():
    #Get input login & password from user with valdiation
    answers = user_credentials()
       
    #Build XML -> return none type that could print out
    xml_data = build_signin_xml(answers['login'], answers['password'])

    #Send XML to web server over the network
    send_post_request("/api/sign-in", xml_data)

def sign_up():
    #Get input logi & password from user with validation
    answers = user_credentials()

    #Build XML -> return none type that could print out
    xml_data = build_signup_xml(answers['login'], answers['password'])

    #Send XML to web server over the network
    send_post_request("/api/sign-up", xml_data)

def sign_out():
    url="/api/sign-out"
    send_get_request(url)