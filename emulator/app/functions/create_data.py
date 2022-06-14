from functions.xml_activity import parse_to_xml

def create_activity_list(response):
    activity = list()

    root = parse_to_xml(response)
    activities = root.findall("Activity")
    for act in activities:
        activity.append(act.findtext("Name"))
    
    return activity

def create_bars_id_list(response):
    step = list()

    root = parse_to_xml(response)
    steps = root.findall("Step")
    for stp in steps:
        step.append(stp.findtext("BarID"))
    
    return step