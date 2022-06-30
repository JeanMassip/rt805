from questions.activity.creation import *
from functions.end_point_requests import *
from functions.create_dict import *
from functions.create_dict import dict_create_activity, dict_create_bar
from functions.date_time import get_datetime_now

def new_activity(session):
    #Get input data from user with validation
    answers = input_new_activity()

    #Build dict new activity
    activity = dict_create_activity(answers['name'], get_datetime_now(), str(" "), session['user_id'])

    #Send post json new activity
    create_activity_request(activity)

    #Get the ID of the activity 
    activities = get_all_activities_by_user(session['user_id'])
    activity['id'] = 77
    for a in activities:
        if a['name'] == activity['name']:
            activity['id'] = a['id']
    return activity

def new_step(session, activity):
    selectBar = True
    step = dict()
    step['bar_id'] = 0

    while selectBar:
        #Get List bar
        bars = get_all_bars()
        
        #Print bars & select a bar name or type a new one
        choice = select_data_or_write(bars, "Select a bar or type a new one: ", "Add new bar")

        #Create a new bar & send it to bdd
        if choice == "Add new bar":
            step['bar_name'] = input_general("Name of the bar: ")
            payload = dict_create_bar(step['bar_name'], 49.000325, 6.325545)
            create_bar(payload)
        else:
            step['bar_name'] = choice[3:]
            selectBar = False

    #Get Bar ID
    for b in bars:
        if b['name'] == step['bar_name']:
            step['bar_id'] = b['id']
            
    #Create step
    payload = dict_create_step(activity['id'], step['bar_id'])

    #Send step to server
    create_step(payload)

    #Get step id
    steps = get_all_steps_by_activity(activity['id'])
    for s in steps:
        if s['bar_id'] == step['bar_id']:
            step['id'] = s['id']
    
    return step    

def new_consumption(session, step):
    selectDrink = True
    consumption = dict()
    consumption['drink_id'] = 0

    while selectDrink:
        #Get List drinks
        drinks = get_all_drinks()
        
        #Print drinks & select a drink name or type a new one
        choice = select_data_or_write(drinks, "Select a drink or type a new one: ", "Add new drink")

        #Create a new drink & send it to bdd
        if choice == "Add new drink":
            consumption['drink_name'] = input_general("Name of the drink: ")
            consumption['drink_degree'] = input_general("Degree of the drink: ")
            consumption['drink_price'] = input_general("Price of the drink: ")
            payload = dict_create_drink(consumption['drink_name'], consumption['drink_degree'], consumption['drink_price'])
            create_drink(payload)
        else:
            consumption['drink_name'] = choice[3:]
            selectDrink = False

    #Get drink ID
    for d in drinks:
        if d['name'] == consumption['drink_name']:
            consumption['drink_id'] = d['id']
    
    #Create consumption
    payload = dict_create_consumption(consumption['drink_id'], step['id'])

    #Send consumption to server
    create_drink(payload)

    #Get consumption ID
    consumptions = get_all_consumptions_by_step(step['id'])
    for c in consumptions:
        if c['name'] == consumption['drink_name']:
            consumption['id'] = c['id']

    return consumption
