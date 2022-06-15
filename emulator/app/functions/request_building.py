import requests
import json
import xml.etree.ElementTree as ET

def send_post_request(url, payload):
    headers = {'Content-Type': 'text/xml'} 
    r = requests.post('http://localhost:5000{}'.format(url), data=payload, headers=headers).text

def send_get_request(url):
    r = requests.get('http://localhost:5000{}'.format(url))

def send_delete_request(url):
    r = requests.delete('http://localhost:5000{}'.format(url))

def send_put_request(url, payload):
    r = requests.put('http://localhost:5000{}'.format(url), data=payload)
    
def get_data_request(url):
    r = requests.get('http://localhost:5000{}'.format(url))
    return r.text




def get_all_activities(user_id):
    return get_data_request("/api/user/{}/activities".format(str(user_id)))

def get_all_steps_of_one_activity(activity_id):
    return get_data_request("/api/activities/{}/steps".format(str(activity_id)))

def get_info_of_one_activity(activity_id):
    return get_data_request("/api/activities/{}".format(str(activity_id)))

def get_all_bars():
    return get_data_request("/api/bars")

def get_all_drinks_of_one_step(step_id):
    return get_data_request("/api/steps/{}/consumptions".format(step_id))

