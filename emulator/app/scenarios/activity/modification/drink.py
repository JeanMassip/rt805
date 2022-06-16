from functions.get_data import *
from questions.activity.modification import modify_main_question_2, modify_second_question_2, select_menu
from functions.request_building import send_delete_request
def show_drinks(session, step_id):
    drinks = get_drinks_info(step_id)
    print("\n****** Drinks *******")
    i=1
    for d in drinks:
        print(" {}. {}".format(i, d['name']))
        print("\tDegree: {}".format(d['degree']))
        print("\tPrice: {}".format(d['price']))
        i+=1
    print("***********************\n")

    return drinks

def show_drinks_action():
    answers = modify_main_question_2("Modify drink", "Return to step list")
    return answers['choice']
        
def modify_drink(drinks, step_id):
    action = modify_second_question_2("Remove drink", "Return to step list")
    
    if action == "Remove drink":
        #Show list of drinks to remove
        drink_list = list()
        for d in drinks:
            drink_list.append(d['name'])
        choice = select_menu("Select a drink to remove: ",drink_list, "Return to step list")
        
        #Get id of the drink and remove it  
        if choice['choice'] != "Return to step list":
            drink_name = choice['choice'][3:]
            drink_id = get_drink_id(step_id, drink_name)
            send_delete_request("/api/consumptions/{}".format(drink_id))
