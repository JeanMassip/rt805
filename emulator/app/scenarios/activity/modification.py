from functions.get_data import get_all_activities, create_activity_list
from questions.activity.modification import select_activity


def show_activities(session):
    #Get all activities from a specific user
    response = get_all_activities(session)
    
    #Create list of all activities
    activities = create_activity_list(response)
    
    #Select an activity
    return select_activity(activities)

def modification(session):
    answers = show_activities(session)

    if answers != "Return to Home page":
        # show_batch(session)
        pass