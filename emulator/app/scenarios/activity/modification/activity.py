from functions.get_data import *
from functions.create_data import create_activity_list
from questions.activity.modification import *
from functions.xml_activity import build_new_activity_xml
from functions.request_building import *

def show_activities(session):
    #Get all activities from a specific user - (Request to server)
    response = get_all_activities(session)
    
    #Create list of all activities
    activities = create_activity_list(response)
    
    #Select an activity within the list
    answers = select_menu("Select an activity", activities, "Return to Home page")
    if answers['choice'] != "Return to Home page":
        answers['choice'] = answers['choice'][3:]
    return answers['choice']

def show_activity_info(session, activity_name):

    #Get ID of the specific activity - (Request to server)
    activity_id = get_activity_id(session, activity_name)

    #Get INFO of the activity with the specific ID - (Request to server)
    activity_info = get_activity_info(session, activity_id)

    #Get number of steps - (Request to server)
    activity_info['number_step'] = get_number_step(activity_id)

    #Get total money spent and the total degree - (Request to server)
    activity_info['money_spent'], activity_info['total_degree'] = get_money_degree(activity_id)

    #Print activity selected with other data
    print("\n*** Activity ***")
    print("Name: " + activity_info['name'])
    print("Started on: " + activity_info['start_time'])
    print("Ended on: " + activity_info['end_time'])
    print("Number of steps: " + str(activity_info['number_step']))
    print("Money spent: " + str(activity_info['money_spent']))
    print("Total Alcohol: " + str(activity_info['total_degree']))
    print("*****************\n")
    
    return activity_info

def show_activities_action():
    answers = modify_main_question("Modify activity", "Visit steps", "Return to activity list")
    return answers['choice']

def modify_activity(activity_info):
    action = modify_second_question("Modify name", "Remove activity", "Return to activity list")
    if action == "Modify name":
        activity_info['name'] = modify_name_question("New name of the activity: ") 
        activity_modified = build_new_activity_xml(activity_info['name'], activity_info['start_time'], activity_info['end_time'], activity_info['user_id'])
        send_put_request("/api/activities/{}".format(activity_info['id']),activity_modified)
    
    if action == "Remove activity":
        send_delete_request("/api/activities/{}".format(activity_info['id']))
    