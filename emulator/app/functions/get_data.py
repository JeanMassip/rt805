from functions.request_building import *
from functions.xml_activity import parse_to_xml


def get_activity_id(session, name):
    id_activity = 0
    
    response = get_all_activities(session['user_id'])
    root = parse_to_xml(response)

    activities = root.findall("Activity")
    for act in activities:
        if act.findtext('Name') == name:
            id_activity = int(act.findtext('ID'))

    return id_activity

def get_last_id_activity(session):
    last_activity = 0

    response = get_all_activities(session['user_id'])
    root = parse_to_xml(response)

    activities = root.findall("Activity")
    for activity in activities:
        if last_activity < int(activity.findtext("ID")):
            last_activity = int(activity.findtext("ID"))
    
    return last_activity

def get_last_id_step(session):
    last_step = 0

    response = get_all_steps_of_one_activity(session['last_activity_id'])
    root = parse_to_xml(response)

    steps = root.findall("Step")
    for step in steps:
        if last_step < int(step.findtext("ID")):
            last_step = int(step.findtext("ID"))

    return last_step

def get_activity_info(session, activity_id):
    activity_info = dict()

    response = get_info_of_one_activity(activity_id)
    root = parse_to_xml(response)

    activity_info['id'] = root.findtext("ID")
    activity_info['name'] = root.findtext("Name")
    activity_info['start_time'] =  root.findtext("StartTime")
    activity_info['end_time'] = root.findtext("EndTime")
    activity_info['user_id'] = root.findtext("UserID")

    return activity_info

def get_bars_info(bars_id):
    bars_list = list()
    response = get_all_bars()
    root = parse_to_xml(response)
    bars = root.findall("Bar")

    for b in bars:
        if b.findtext("ID") in bars_id:
            bar_info = dict()
            bar_info['name'] = b.findtext("Name")
            bar_info['id'] = b.findtext("ID")
            bars_list.append(bar_info)
    return bars_list

def get_number_step(activity_id):
    response = get_all_steps_of_one_activity(activity_id)
    root = parse_to_xml(response)
    steps = root.findall("Step")
    i=0
    for s in steps:
        i+=1
    return i
    

def get_money_spent(activity_id):
    #Get all step ID of a regarding activity
    steps_id = list()
    response = get_all_steps_of_one_activity(activity_id)
    root = parse_to_xml(response)
    steps = root.findall("Step")
    
    #Get all steps ID xml from their xml
    for s in steps:
        steps_id.append(s.findtext("ID"))

    #Get all Drinks of each step ID
    money_spent = 0
    for stp_id in steps_id:
        response = get_all_drinks_of_one_step(stp_id)
        root = parse_to_xml(response)
        drinks = root.findall("Drink")

        #Get all Price of each drinks
        for d in drinks:
            money_spent += int(d.findtext("Price"))

    return money_spent   
        
def get_money_degree(activity_id):
    #Get all step ID of a regarding activity
    steps_id = list()
    response = get_all_steps_of_one_activity(activity_id)
    root = parse_to_xml(response)
    steps = root.findall("Step")
    
    #Get all steps ID xml from their xml
    for s in steps:
        steps_id.append(s.findtext("ID"))

    #Get all Drinks of each step ID
    money_spent = 0
    total_degree = 0.0
    for stp_id in steps_id:
        response = get_all_drinks_of_one_step(stp_id)
        root = parse_to_xml(response)
        drinks = root.findall("Drink")

        #Get all Price of each drinks
        for d in drinks:
            money_spent += int(d.findtext("Price"))
            total_degree += float(d.findtext("Degree"))

    return money_spent, round(total_degree,2)

