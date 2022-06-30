from .functions import *

def creation(session):
    addStep = True
    addDrink = True

    #Add new activity
    activity = new_activity(session)

    #Add new step
    while addStep:
        answers = next_move_question("Add a new step", "Finish activity")
        if answers['move'] == "Add a new step":
            step = new_step(session, activity)

            #Add new drink
            while addDrink:    
                answers = next_move_question("Add a new consumption", "Finish step")
                if answers['move'] == "Add a new consumption":
                    new_consumption(session,step)
                else:
                    addDrink = False
            addDrink = True
        else:
            addStep = False


    