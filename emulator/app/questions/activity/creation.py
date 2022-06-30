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

def input_new_activity():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name of the activity: ',
            'validate': password_validation,
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers

def select_data_or_write(bars, main_msg, type_msg):
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': main_msg,
            'choices': [''
            ]
        },
    ]
    questions[0]['choices'].remove('')
    i=1
    for b in bars:
        questions[0]['choices'].append(str(i) + ". " + b['name'])
        i=i+1
    questions[0]['choices'].append(type_msg)
    answers = prompt(questions, style=custom_style_2)
    return answers['choice']

def input_general(msg):
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': msg,
            'validate': password_validation,
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers['name']

def input_new_drink():
    questions = [
        {
            'type': 'input',
            'name': 'drink_name',
            'message': 'Name of the consumption: ',
            'validate': password_validation,
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers

def next_move_question(fist_option, second_option):
    questions = [
        {
            'type': 'list',
            'name': 'move',
            'message': 'What\'s your next move? ',
            'choices': [
                '{}'.format(fist_option),
                '{}'.format(second_option),
            ]
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers

