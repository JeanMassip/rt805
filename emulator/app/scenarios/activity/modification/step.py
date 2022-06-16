from functions.get_data import *
from functions.request_building import get_all_steps_of_one_activity,send_delete_request
from functions.create_data import create_bars_id_list
from questions.activity.modification import *
from functions.xml_activity import build_new_bar_xml

def show_steps(session, activity_info):
    # #Get all steps regarding the specific activity - (Request to server)
    response = get_all_steps_of_one_activity(activity_info['id'])

    #Create list of all id of bar
    bars_id = create_bars_id_list(response)
    
    #Get bar info (name + id) - (Request to server)
    bars_info = get_bars_info(bars_id)

    #Split bar info to extract bars name
    bars_names = list()
    for bn in bars_info:
        bars_names.append(bn['name'])

    #Select a step
    answers = select_menu("Select a step: ", bars_names, "Return to activity list")
    choice = answers['choice']

    #Form a couple with the bar name selected and its id
    bar_selected_info = dict()
    if choice != "Return to activity list":
        bar_selected_info['name'] = choice[3:]
        for bn in bars_info:
            if bn['name'] == bar_selected_info['name']:
                bar_selected_info['id'] = bn['id']

    
    return bar_selected_info, choice

def show_step_info(session, activity_info, bar_info):

    #Get step id of the concerned activity - (Request to server)
    step_id = get_step_id(activity_info, bar_info)
    
    #Get all drinks of the step - (Request to server)
    drinks = get_drinks_info(step_id)

    #Caculation data
    number_drinks = 0
    money_spent = 0
    avr_degree = 0.0
    for d in drinks:
        money_spent += int(d['price'])
        avr_degree += float(d['degree'])
        number_drinks+=1
    avr_degree /= number_drinks
    total_degree = (number_drinks*100*(avr_degree/100)*0.8)/(0.7*75)
    total_degree = round(total_degree,2)

    #Get location of the bar
    bar_info['location'] = get_bar_location(step_id)

    print("\n*** " + bar_info['name'] + " ***")
    print("Location: " + bar_info['location'])
    print("Drinks: ")
    i=1
    for d in drinks:
        print(" {}. {}".format(i, d['name']))
        print("\tDegree: {}".format(d['degree']))
        print("\tPrice: {}".format(d['price']))
        i+=1
    print("Money spent: " + str(money_spent))
    print("Total Alcohol: "+ str(total_degree))
    print("*****************************\n")

    return step_id

def show_steps_action():
    answers = modify_main_question("Modify step", "Visit drinks", "Return to step list")
    return answers['choice']

def modify_step(bar_info, step_id, activity_id):
    action = modify_second_question_step("Remove step", "Return to step list")
    # if action == "Modify bar name":        
    #     #Create new bar and send to db
    #     bar_info['name'] = modify_name_question("New name of the bar: ")
    #     position = bar_info["location"].split(" ")
    #     bar_modified = build_new_bar_xml(bar_info['name'], position[0], position[1])
    #     send_post_request("/api/bar",bar_modified)
    #     #Get new_bar_id
    #     bar_id = get_bar_id(bar_info['name'])
    #     print("Bar id: " +str(bar_id))
    #     #Get step with old id
    #     step = get_step_info(step_id, activity_id)
    #     #Create new step with new id
        #Change bar id of the step
    if action == "Remove step":
        send_delete_request("/api/steps/{}".format(step_id))