from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

#************************************** Sign *************************************

@app.route('/api/users/sign-in', methods=['GET', 'POST'])
def signIn():
    print(request.data)
    return "OK"

@app.route('/api/users/register', methods=['GET', 'POST'])
def signUp():
    print(request.data)
    return "OK"

@app.route('/api/users/sign-out', methods=['GET', 'POST'])
def signOut():
    print("GET request")
    return "OK"

#************************************** Activities *************************************

@app.route('/api/activities', methods=['GET', 'POST'])
def activities():
    print(request.data)
    return "OK"

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
    print(request.data)
    return "OK"

@app.route('/api/activities/<id>/steps', methods=['GET', 'POST'])
def idLastSteps(id):
    print('activity {}'.format(id))
    return render_template('id_last_step.html',id=id)

@app.route('/api/steps/<id>/bar', methods=['GET', 'POST'])
def bar(id):
    return render_template('bar.html')

#************************************** consumptions *************************************
@app.route('/api/consumptions', methods=['GET', 'POST'])
def addDrink():
    if request.method == 'POST':
        return "method post"
    else:
        return "method get"

@app.route('/api/steps/<id>/consumptions', methods=['GET', 'POST'])
def getDrinkOfaStep(id):
    return render_template('drinks.html',id=id)
        

#************************************** bar *************************************
@app.route('/api/bars', methods=['GET', 'POST'])
def barList():
    return render_template('barList.html')

@app.route('/api/bar/<id>', methods=['GET', 'POST'])
def barInfo(id):
    return render_template('bar_info.html', id=id)

@app.route('/api/bar', methods=['GET', 'POST'])
def barCreation():
    print(request.data)
    return "bar created"

#************************************** drink *************************************
@app.route('/api/drink', methods=['GET', 'POST'])
def drinkList():
    return render_template('drinks.html')