from questions.activity.modification import *
from functions.end_point_requests import *
from functions.create_dict import *

def show_steps(session, activity):
    step = dict()

    #Show all bars
    steps = get_all_steps_by_activity(activity['id'])
    barnames = list()
    for s in steps:
        bar = get_bar_data_by_bar(s['bar_id'])
        barnames.append(bar[0]['name'])

    #Select a bar
    choice = select_menu("Select a step: ", barnames, "Return to activity list")

    #Get step information (id, activity, bar_id, bar_name, bar_lon, bar_lat)
    if choice != "Return to activity list":
        step['activity'] = activity['id']
        step['bar_name'] = choice[3:]
        bars = get_all_bars()
        for b in bars:
            if b['name'] == step['bar_name']:
                step['bar_id'] = b['id']
                step['bar_position_lon'] = b['position_lon']
                step['bar_position_lat'] = b['position_lat']
        
        for s in steps:
            if s['bar_id'] == step['bar_id']:
                step['id'] = s['id']
        bar = get_bar_data_by_bar(s['bar_id'])
        barnames.append(bar[0]['name'])
        

    
    return step, choice

def show_step_info(session, activity, step):

    consumptions = get_all_consumptions_by_step(step['id'])

    #Caculation data
    number_consumption = 0
    total_money = 0
    avr_degree = 0.0
    for c in consumptions:
        total_money += int(c['price'])
        avr_degree += float(c['degree'])
        number_consumption+=1
    avr_degree /= number_consumption
    total_degree = (number_consumption*100*(avr_degree/100)*0.8)/(0.7*75)
    step['total_degree'] = round(total_degree,2)
    step['total_money'] = total_money
    step['total_consumption'] = number_consumption

    #Present step selected
    print("\n***** " + step['bar_name'] + " *****")
    print("position_lon: " + str(step['bar_position_lon']))
    print("position_lat: " + str(step['bar_position_lat']))
    print("Drinks: "+ str(step['total_consumption']))
    print("Money spent: " + str(step['total_money']))
    print("Total Alcohol: "+ str(step['total_degree']))
    print("***************************\n")

    return step

def show_steps_action():
    answers = modify_main_question("Modify step", "Visit drinks", "Return to step list")
    return answers['choice']

def modify_step(step):
    action = modify_second_question_2("Remove step", "Return to step list")
    # if action == "Modify bar name":        
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
        remove_step(step['id'])