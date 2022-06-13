from questions.activity import input_new_activity, input_new_step, input_new_drink
from functions.xml_activity import build_new_activity_xml, build_new_step_xml
from functions.request_building import send_post_request
from functions.date_time import get_datetime_now
from functions.get_data import get_last_id_activity

def new_activity(userId):
    #Get input data from user with validation
    answers = input_new_activity()

    #Build xml new activity
    xml_data = build_new_activity_xml(answers['name'], get_datetime_now(), str(" "), userId)

    #Send post xml new activity
    send_post_request("/api/activities", xml_data)

def new_step(userId):
    #Get bar name 
    answers = input_new_step()

    #Build xml new step
    xml_data = build_new_step_xml(get_last_id_activity(userId), answers['bar_name'])

    #Send post xml new activity
    send_post_request("/api/steps", xml_data)

def new_drink(userId):
    #Get bar name 
    answers = input_new_drink()

    #Get id of the last step created

def creation(userId):
    new_activity(userId)
    new_step(userId)
    new_drink(userId)



    