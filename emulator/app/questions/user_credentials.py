#!/bin/python3.8
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
from functions.validation import login_validation, password_validation

def user_credentials():
    questions = [
        {
            'type': 'input',
            'name': 'login',
            'message': 'Enter login (email expected - xxx@www.yy): ',
            'validate': login_validation,
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Enter password  (a-zA-Z0-9- from 5 to 20 characters): ',
            'validate': password_validation,
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers