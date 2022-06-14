from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
from functions.validation import login_validation, password_validation

def select_menu(msg, names, return_page):
    
    questions = [
        {
            'type': 'list',
            'name': 'choice',
            'message': msg,
            'choices': [''
            ]
        },
    ]

    questions[0]['choices'].remove('')
    i=1
    for n in names:
        questions[0]['choices'].append(str(i) + ". " + str(n))
        i+=1
    questions[0]['choices'].append(return_page)

    answers = prompt(questions, style=custom_style_2)
    return answers

def modify_main_question(fst_opt, scd_opt, thd_opt):
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Action:',
            'choices': [
                fst_opt, scd_opt, thd_opt,
            ]
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers

def modify_activity_action_menu():
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Action:',
            'choices': [
                'Modify name',
                'Remove activity',
                'Return to the activity menu',
            ]
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers

def new_activity_name_question():
    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'New name of the activity: ',
            'validate': password_validation,
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers['name']

#*********************** Step ************************
