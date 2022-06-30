import requests
import json

#*** Server address ***
serverAddr = "http://localhost:5000"

# Send requests
def send_post_request(end_point, payload):
    headers = {'Content-Type': 'text/json'}
    url = serverAddr + end_point
    r = requests.post(url, data=json.dumps(payload), headers=headers).text

def send_get_request(end_point):
    url = serverAddr + end_point
    r = requests.get(url)
    if r.text != "OK":
        return json.loads(r.text)

def send_put_request(end_point, payload):
    headers = {'Content-Type': 'text/json'} 
    url = serverAddr + end_point
    r = requests.put(url, data=payload, headers=headers).text

def send_delete_request(end_point):
    url = serverAddr + end_point
    r = requests.delete(url)



