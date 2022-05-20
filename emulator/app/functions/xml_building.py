import xml.etree.ElementTree as ET


def build_signin_xml(login, password):
    url="/api/sign-in"

    connexion = ET.Element("Connexion")
    ET.SubElement(connexion, "Email").text = login
    ET.SubElement(connexion, "Password").text = password

    tree = ET.ElementTree(connexion)

    #dump(tree) -> print out
    return ET.dump(tree)

def build_signup_xml(login, password):
    url="/api/register"

    inscription = ET.Element("Inscription")
    ET.SubElement(inscription, "Email").text = login
    ET.SubElement(inscription, "Password").text = password

    tree = ET.ElementTree(inscription)

    #dump(tree) -> print out
    return ET.dump(tree)