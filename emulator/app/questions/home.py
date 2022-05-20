#!/bin/python3.8

# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from examples import custom_style_2

def home_question():
    questions = [
        {
            'type': 'list',
            'name': 'first_move',
            'message': 'What\'s your first move?',
            'choices': [
                'Sign in',
                'Sign up',
            ]
        },
    ]

    answers = prompt(questions, style=custom_style_2)
    # pprint(answers)
    
    return answers['first_move']