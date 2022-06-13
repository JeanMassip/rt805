from functions.request_building import get_all_activities
from functions.xml_activity import parse_to_xml

def get_last_id_activity(userId):
    last_activity = 0

    response = get_all_activities("/api/user/{}/activites".format(userId))
    root = parse_to_xml(response)

    activities = root.findall("Activity")
    for activity in activities:
        if last_activity < int(activity.findtext("ID")):
            last_activity = int(activity.findtext("ID"))
    
    return last_activity




