from .activity import * 
from .step import * 
from .drink import *

def modification(session):
    modificationActivity = True
    
    while modificationActivity:

        #Show activities and return actions
        activity_name = show_activities(session)

        #Show activities details and return action
        if activity_name != "Return to Home page":
            activity_info = show_activity_info(session, activity_name)
            choice = show_activities_action()

            #Modify activity
            if choice == "Modify activity":
                modify_activity(activity_info)

            #Visit steps
            if choice == "Visit steps":

                modificationStep = True
                while modificationStep:
                    #Show all steps and return action
                    bar_info, choice = show_steps(session, activity_info)
                    
                    #Show step detail and return action
                    if choice != "Return to activity list":
                        step_id = show_step_info(session, activity_info, bar_info)
                        choice = show_steps_action()

                        #Modify step
                        if choice == "Modify step":
                            modify_step(bar_info, step_id, activity_info['id'])

                        if choice == "Visit drinks":
                            drinks = show_drinks(session, step_id)
                            choice = show_drinks_action()

                            if choice != "Return to step list":
                                modify_drink(drinks, step_id)
                    else:
                        modificationStep = False
        else:
            modificationActivity = False