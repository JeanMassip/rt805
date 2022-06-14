from .functions import *
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



    