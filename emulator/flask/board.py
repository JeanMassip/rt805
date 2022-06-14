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

@app.route('/api/user/<id>/activities', methods=['GET', 'POST'])
def idlastactivities(id):
    print('user {}'.format(id))
    return render_template('id_last_activity.html',id=id)

@app.route('/api/activities/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def activityInfo(id):
    if request.method == 'POST':
        return render_template('activity_info.html',id=id)
    elif request.method == 'DELETE':
        return "method DELETE"
    elif request.method == 'PUT':
        return "method PUT"
    else:
        return render_template('activity_info.html',id=id)
    


#************************************** steps *************************************

@app.route('/api/steps', methods=['GET', 'POST'])
def addStep():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/activities/<id>/steps', methods=['GET', 'POST'])
def idLastSteps(id):
    print('activity {}'.format(id))

    return render_template('id_last_step.html',id=id)

#************************************** consumptions *************************************
@app.route('/api/consumptions', methods=['GET', 'POST'])
def addDrink():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

#************************************** consumptions *************************************
@app.route('/api/bars', methods=['GET', 'POST'])
def barList():
    return render_template('barList.html')
