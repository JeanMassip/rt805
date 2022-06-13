from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
from functions.validation import login_validation, password_validation

def home_question():
    questions = [
        {
            'type': 'list',
            'name': 'activity',
            'message': 'Home page! What do you want to do next?',
            'choices': [
                'Start a new activity',
                'Visit activities',
                'Sign out',
            ]
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers['activity']