from questions.activity.modification import modify_main_question_2, modify_second_question_2, select_menu
from functions.end_point_requests import *

def show_drinks(session, step):
    consumptions = get_all_consumptions_by_step(step['id'])
    print("\n****** Drinks *******")
    i=1
    for c in consumptions:
        print(" {}. {}".format(i, c['name']))
        print("\tDegree: {}".format(c['degree']))
        print("\tPrice: {}".format(c['price']))
        i+=1
    print("***********************\n")

    return consumptions

def show_drinks_action():
    answers = modify_main_question_2("Modify drink", "Return to step list")
    return answers['choice']
        
def modify_consumption(consumptions, step):
    action = modify_second_question_2("Remove drink", "Return to step list")
    
    if action == "Remove drink":
        #Show list of drinks to remove
        drink_name = list()
        for c in consumptions:
            drink_name.append(c['name'])
        choice = select_menu("Select a drink to remove: ",drink_name, "Return to step list")
        
        #Get id of the drink and remove it  
        if choice != "Return to step list":
            drink_to_delete = choice[3:]
            for c in consumptions:
                if c['name'] == drink_to_delete:
                    remove_drink(c['id'])

