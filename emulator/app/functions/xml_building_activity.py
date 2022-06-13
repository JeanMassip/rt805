import xml.etree.ElementTree as ET


def build_new_activity_xml(name, startTime, endTime, userId):

    create_activity = ET.Element("CreateActivity")
    ET.SubElement(create_activity, "Name").text = name
    ET.SubElement(create_activity, "StartTime").text = startTime
    ET.SubElement(create_activity, "EndTime").text = endTime
    ET.SubElement(create_activity, "UserID").text = userId

    tree = ET.ElementTree(create_activity)

    #dump(tree) -> print out
    return ET.dump(tree)