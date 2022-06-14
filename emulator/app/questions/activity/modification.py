from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2
from functions.validation import login_validation, password_validation

def select_activity(activities):
    
    questions = [
        {
            'type': 'list',
            'name': 'activity',
            'message': 'Select an activity:',
            'choices': [''
            ]
        },
    ]

    questions[0]['choices'].remove('')
    i=1
    for act in activities:
        questions[0]['choices'].append(str(i) + ". " + str(act))
        i+=1
    questions[0]['choices'].append('Return to Home page')

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    return answers

def modify_activity_main_question():
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Action:',
            'choices': [
                'Modify activity',
                'Modify steps',
                'Return to the list of activities',
            ]
        },
    ]
    answers = prompt(questions, style=custom_style_2)
    return answers