from .activity import * 
from .step import * 
from .drink import *

def modification(session):
    modificationActivity = True
    
    while modificationActivity:
        #Show activities and return actions
        activity,choice = show_activities(session)

        #Show activities details and return action
        if choice != "Return to Home page":
            activity = show_activity_info(session, activity)
            choice = show_activities_action()

            #Modify activity
            if choice == "Modify activity":
                activity = modify_activity(activity)

            #Visit steps
            if choice == "Visit steps":

                modificationStep = True
                while modificationStep:
                    #Show all steps and return action
                    step, choice = show_steps(session, activity)

                    #Show step details and return action
                    if choice != "Return to activity list":
                        step = show_step_info(session, activity, step)
                        choice = show_steps_action()

                        #Modify step
                        if choice == "Modify step":
                            modify_step(step)

                        if choice == "Visit drinks":
                            consumptions = show_drinks(session, step)
                            choice = show_drinks_action()

                            if choice != "Return to step list":
                                modify_consumption(consumptions, step)
                    else:
                        modificationStep = False
        else:
            modificationActivity = False