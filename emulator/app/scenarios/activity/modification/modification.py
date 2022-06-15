from .activity import * 
from .step import * 

def modification(session):
    modificationActivity = True

    while modificationActivity:

        #Show activities and return actions
        activity_name = show_activities(session)
        
        if activity_name != "Return to Home page":
            #Show detail of the activity
            activity_info = show_activity_info(session, activity_name)

            #Show action menu and return action
            choice = show_activities_action()

            if choice == "Modify activity":
                modify_activity(activity_info)

            if choice == "Modify steps":
                bar_info = show_steps(session, activity_info)
                show_step_info(session, activity_info, bar_info)
        #     # #Modify step
        #     # elif answers['action'] == "Modify steps":

        #     #     answers = show_steps(session, activity_info)
        #     #     if answers['choice'] != "Return to activity list":
        #     #         modify_step(answers)
                
        #     else:
        #         pass

        # else:
        #     modificationActivity = False