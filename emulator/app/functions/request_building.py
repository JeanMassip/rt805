import requests
import json
import xml.etree.ElementTree as ET

def send_post_request(url, payload):
    headers = {'Content-Type': 'text/xml'} 
    r = requests.post('http://localhost:5000{}'.format(url), data=payload, headers=headers).text

def send_get_request(url):
    r = requests.get('http://localhost:5000{}'.format(url))
    
def get_all_activities(url):
    r = requests.get('http://localhost:5000{}'.format(url))
    return r.text