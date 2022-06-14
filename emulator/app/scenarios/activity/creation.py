from questions.activity.creation import input_new_activity, input_new_step, input_new_drink, next_move_question
from functions.xml_activity import build_new_activity_xml, build_new_step_xml, build_new_drink_xml
from functions.request_building import send_post_request
from functions.date_time import get_datetime_now
from functions.get_data import get_last_id_activity, get_last_id_step

def new_activity(session):
    #Get input data from user with validation
    answers = input_new_activity()

    #Build xml new activity
    xml_data = build_new_activity_xml(answers['name'], get_datetime_now(), str(" "), session['user_id'])

    #Send post xml new activity
    send_post_request("/api/activities", xml_data)

    #Get id of the last activity created
    session['last_activity_id'] = get_last_id_activity(session)

    return session['last_activity_id']

def new_step(session):
    #Get bar name 
    answers = input_new_step()

    #Build xml new step
    xml_data = build_new_step_xml(session['last_activity_id'], answers['bar_name'])

    #Send post xml new activity
    send_post_request("/api/steps", xml_data)

    #Get id of the last activity created
    session['last_step_id'] = get_last_id_step(session)

    return session['last_step_id']

def new_drink(session):
    #Get bar name 
    answers = input_new_drink()

    #Build xml new step
    xml_data = build_new_drink_xml(session['last_step_id'], answers['drink_name'])

    #Send post xml new activity
    send_post_request("/api/consumptions", xml_data)

def creation(session):
    addStep = True
    addDrink = True

    #Add new activity
    session['last_activity_id'] = new_activity(session)

    #Add new step
    while addStep:
        answers = next_move_question("Add a new step", "Finish activity")
        if answers['move'] == "Add a new step":
            session['last_step_id'] = new_step(session)

            #Add new drink
            while addDrink :
                answers = next_move_question("Add a new drink", "Finish step")
                if answers['move'] == "Add a new drink":
                    new_drink(session)
                else:
                    addDrink = False

            addDrink = True
        else:
            addStep = False



    