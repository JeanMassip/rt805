from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

#************************************** Sign *************************************

@app.route('/api/users/sign-in', methods=['GET', 'POST'])
def signIn():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/users/register', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/users/sign-out', methods=['GET', 'POST'])
def signOut():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

#************************************** Activities *************************************

@app.route('/api/activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/user/<id>/activites', methods=['GET', 'POST'])
def idlastactivities(id):
    print('user {}'.format(id))

    return render_template('id_last_activity.html',id=id)


#************************************** steps *************************************

@app.route('/api/steps', methods=['GET', 'POST'])
def addStep():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"