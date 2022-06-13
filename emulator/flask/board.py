from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api/sign-in', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/sign-out', methods=['GET', 'POST'])
def signOut():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"
