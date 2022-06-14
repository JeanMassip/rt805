from functions.xml_activity import parse_to_xml

def create_activity_list(response):
    activity = list()

    root = parse_to_xml(response)
    activities = root.findall("Activity")
    for act in activities:
        activity.append(act.findtext("Name"))
    
    return activity