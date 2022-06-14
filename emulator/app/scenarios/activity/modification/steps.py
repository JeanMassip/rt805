from functions.get_data import get_all_steps, get_bars_name
from functions.create_data import create_bars_id_list
from questions.activity.modification import select_menu

def show_steps(session, activity_info):
    # #Get all steps regarding the specific activity
    response = get_all_steps(activity_info['id'])

    #Create list of all id of bar
    bars_id = create_bars_id_list(response)
    
    #Get bar names
    bars_names = get_bars_name(bars_id)

    #Select a step
    return select_menu("Select a step: ", bars_names, "Return to activity list")