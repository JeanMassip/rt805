from questions.activity import input_new_activity
from functions.xml_building_activity import build_new_activity_xml
from functions.request_building import send_post_request
from functions.date_time import get_datetime_now
from random import randint

def new_activity():
    #Get input data from user with validation
    answers = input_new_activity()

    #Build xml new activity
    xml_data = build_new_activity_xml(answers['name'], get_datetime_now(), str(" "), str(randint(1,10)))

    #Send post xml new activity
    send_post_request("/api/activities", xml_data)

    