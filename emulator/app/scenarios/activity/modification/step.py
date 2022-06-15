from functions.get_data import *
from functions.request_building import get_all_steps_of_one_activity
from functions.create_data import create_bars_id_list
from questions.activity.modification import select_menu

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

    #Form a couple with the bar name selected and its id
    bar_selected_info = dict()
    bar_selected_info['name'] = answers['choice'][3:]
    for bn in bars_info:
        if bn['name'] == bar_selected_info['name']:
            bar_selected_info['id'] = bn['id']
    
    return bar_selected_info

def show_step_info(session, activity_info, bar_info):
    pass

def modify_step(answers):
    bar_name = answers['choice'][3:]
    
    #Get all information about the specfic step