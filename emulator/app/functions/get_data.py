from functions.request_building import get_data_request
from functions.xml_activity import parse_to_xml

def get_all_activities(user_id):
    return get_data_request("/api/user/{}/activities".format(str(user_id)))

def get_all_steps(activity_id):
    return get_data_request("/api/activities/{}/steps".format(str(activity_id)))

def get_activity_id(session, name):
    id_activity = 0
    
    response = get_all_activities(session['user_id'])
    root = parse_to_xml(response)

    activities = root.findall("Activity")
    for act in activities:
        if act.findtext('Name') == name:
            id_activity = int(act.findtext('ID'))

    return id_activity

def get_last_id_activity(session):
    last_activity = 0

    response = get_all_activities(session['user_id'])
    root = parse_to_xml(response)

    activities = root.findall("Activity")
    for activity in activities:
        if last_activity < int(activity.findtext("ID")):
            last_activity = int(activity.findtext("ID"))
    
    return last_activity

def get_last_id_step(session):
    last_step = 0

    response = get_all_steps(session['last_activity_id'])
    root = parse_to_xml(response)

    steps = root.findall("Step")
    for step in steps:
        if last_step < int(step.findtext("ID")):
            last_step = int(step.findtext("ID"))

    return last_step

def get_activity_info(session, activity_id):
    activity_info = dict()

    response = get_data_request("/api/activities/{}".format(str(activity_id)))
    root = parse_to_xml(response)

    activity_info['id'] = root.findtext("ID")
    activity_info['name'] = root.findtext("Name")
    activity_info['start_time'] =  root.findtext("StartTime")
    activity_info['end_time'] = root.findtext("EndTime")
    activity_info['user_id'] = root.findtext("UserID")

    return activity_info

def get_bars_name(bars_id):
    bar_list = list()
    response = get_data_request("/api/bars")
    root = parse_to_xml(response)
    bars = root.findall("Bar")

    for b in bars:
        if b.findtext("ID") in bars_id:
            bar_list.append(b.findtext("Name"))

    return bar_list





