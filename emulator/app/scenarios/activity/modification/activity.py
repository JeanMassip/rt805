from questions.activity.modification import *
from functions.end_point_requests import *
from functions.create_dict import *

def show_activities(session):
    activity = dict()

    #Get all activities from a specific user - (Request to server)
    activities = get_all_activities_by_user(session['user_id'])
    
    #Select an activity within the list
    activity_names = list()
    for a in activities:
        activity_names.append(a['name'])

    choice = select_menu("Select an activity", activity_names, "Return to Home page")
    if choice != "Return to Home page":
        activity['name'] = choice[3:]
    
        #Gather other information about the activity selected 
        for a in activities:
            if a['name'] == activity['name']:
                activity['id'] = a['id']
                activity['start_time'] = a['start_time']
                activity['end_time'] = a['end_time']
                activity['user_id'] = a['user_id']

    return activity, choice



def show_activity_info(session, activity):
    total_step = 0
    total_money = 0
    total_degree = 0
    total_consumption = 0

    #Get all steps regardin activity id - (Request to server)
    steps = get_all_steps_by_activity(activity['id'])
    
    #Get total steps + total money + total degree
    for s in steps:

        #Get total step
        total_step+=1

        #Get total money + total degree
        consumptions = get_all_consumptions_by_step(s['id'])
        for c in consumptions:
            total_consumption +=1 
            total_money += c['price']
            total_degree += c['degree']

    #Update degree
    activity['total_step'] = total_step
    activity['total_money'] = total_money
    activity['total_consumption'] = total_consumption
    activity['total_degree'] = round(((25*total_consumption)*((total_degree/total_consumption)/100)*0.80)/(0.7*75),2)

    #Print activity selected with other data
    print("\n*** Activity ***")
    print("Name: " + activity['name'])
    print("Started on: " + activity['start_time'])
    print("Ended on: " + activity['end_time'])
    print("Number of steps: " + str(activity['total_step']))
    print("Money spent: " + str(activity['total_money']))
    print("Total Alcohol: " + str(activity['total_degree']))
    print("*****************\n")
    
    return activity

def show_activities_action():
    answers = modify_main_question("Modify activity", "Visit steps", "Return to activity list")
    return answers['choice']

def modify_activity(activity):
    action = modify_second_question("Modify name", "Remove activity", "Return to activity list")
    if action == "Modify name":
        activity['name'] = modify_name_question("New name of the activity: ") 
        payload = dict_create_activity(activity['name'], activity['start_time'], activity['end_time'], activity['user_id'])
        modify_activity_request(activity['id'], payload)

    if action == "Remove activity":
        remove_activity(activity['id'])
        
    return activity
    