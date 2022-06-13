import xml.etree.ElementTree as ET


def build_new_activity_xml(name, startTime, endTime, userId):

    create_activity = ET.Element("CreateActivity")
    ET.SubElement(create_activity, "Name").text = name
    ET.SubElement(create_activity, "StartTime").text = startTime
    ET.SubElement(create_activity, "EndTime").text = endTime
    ET.SubElement(create_activity, "UserID").text = str(userId)

    tree = ET.ElementTree(create_activity)

    #dump(tree) -> print out
    return ET.dump(tree)

def build_new_step_xml(activity, barname):

    create_step = ET.Element("CreateStep")
    ET.SubElement(create_step, "Activity").text = str(activity)
    ET.SubElement(create_step, "Bar").text = barname

    tree = ET.ElementTree(create_step)

    #dump(tree) -> print out
    return ET.dump(tree)

def build_new_drink_xml(step, drinkname):

    create_drink = ET.Element("Consumption")
    ET.SubElement(create_drink, "DrinkID").text = drinkname
    ET.SubElement(create_drink, "StepID").text = str(step)

    tree = ET.ElementTree(create_drink)

    #dump(tree) -> print out
    return ET.dump(tree)

def parse_to_xml(string):
    if string[1] != "?":
        string = "<?xml version=\"1.0\" encoding=\"utf-16\"?>" + string
    root = ET.fromstring(string)

    return root