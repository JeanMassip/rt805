from functions.get_data import get_all_activities, get_activity_id, get_activity_info
from functions.create_data import create_activity_list
from questions.activity.modification import *
from functions.xml_activity import build_new_activity_xml
from functions.request_building import send_post_request, send_delete_request

def show_activities(session):
    #Get all activities from a specific user
    response = get_all_activities(session)
    
    #Create list of all activities
    activities = create_activity_list(response)
    
    #Select an activity
    return select_activity(activities)

def modify_activity_menu(session, answers):
    activity_name = answers['activity'][3:]

    #Get id of the specific activity
    activity_id = get_activity_id(session, activity_name)

    #Get Activity info
    activity_info = get_activity_info(session, activity_id)

    #Print activity
    print("*** Activity: ***")
    print("Name: " + activity_info['name'])
    print("Started pn: " + activity_info['start_time'])
    print("Ended on: " + activity_info['end_time'])
    print("*****************")

    #Set action concerning the activity
    answers = modify_activity_main_question()
    return answers, activity_info

def modify_activity(activity_info):
    answers = modify_activity_action_question()

    if answers['action'] == "Modify name":
        activity_info['name'] = new_activity_name_question() 
        activity_modified = build_new_activity_xml(activity_info['name'], activity_info['start_time'], activity_info['end_time'], activity_info['user_id'])
        send_post_request("/api/activities/{}".format(activity_info['id']),activity_modified)
    
    if answers['action'] == "Remove activity":
        send_delete_request("/api/activities/{}".format(activity_info['id']))
    

def modification(session):
    modificationActivity = True

    while modificationActivity:

        #Show activities and return actions
        answers = show_activities(session)
        if answers['activity'] != "Return to Home page":

            #Get the action selected regarding the activity
            answers, activity_info = modify_activity_menu(session, answers)
            if answers['action'] == "Modify activity":
                #Modify activity
                modify_activity(activity_info)

            elif answers['action'] == "Modify steps":
                # modify_step_menu()
                pass
            else:
                pass

        else:
            modificationActivity = False