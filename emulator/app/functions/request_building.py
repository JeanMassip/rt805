import requests

def send_post_request(url, payload):
    headers = {'Content-Type': 'text/xml'} 
    r = requests.post('http://localhost:8000', data=payload, headers=headers).text
    print("request: {}".format(r))

def send_get_request(url):
    r = request.get('http://localhost:8000')
    print("request: {}".format(r))
    
    