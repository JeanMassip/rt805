from .activity import * 
from .steps import * 

def modification(session):
    modificationActivity = True

    while modificationActivity:

        #Show activities and return actions
        answers = show_activities(session)
        if answers['choice'] != "Return to Home page":

            #Get the action selected regarding the activity
            answers, activity_info = modify_activity_menu(session, answers)

            #Modify activity
            if answers['action'] == "Modify activity":
                modify_activity(activity_info)
            
            #Modify step
            elif answers['action'] == "Modify steps":
                answers = show_steps(session, activity_info)
                # modify_step_menu()
                
            else:
                pass

        else:
            modificationActivity = False