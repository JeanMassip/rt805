# *** Sign ***
def dict_sign_in(email, password):
    d = dict()
    d['email'] = email
    d['password'] = password
    return d

def dict_sign_up(email, password):
    return dict_sign_in(email, password)

#*** Activity ***
def dict_create_activity(name, start_time, end_time, user_id):
    d = dict()
    d['name'] = name
    d['start_time'] = start_time
    d['end_time'] = end_time
    d['user_id'] = user_id
    return d

def dict_modify_activity(name, start_time, end_time):
    d = dict()
    d['name'] = name
    d['start_time'] = start_time
    d['end_time'] = end_time
    return d

#*** Steps ***
def dict_create_step(activity_id, bar_id):
    d = dict()
    d['activity'] = activity_id
    d['bar'] = bar_id
    return d

#*** Consumptions ***
def dict_create_consumption(drink_id, step_id):
    d = dict()
    d['drink_id'] = drink_id
    d['step_id'] = step_id
    return d

#*** Bar ***
def dict_create_bar(name, position_lon, position_lat):
    d = dict()
    d['name'] = name
    d['position_lon'] = position_lon
    d['position_lat'] = position_lat
    return d

#*** Drink ***
def dict_create_drink(name, degree, price):
    d = dict()
    d['name'] = name
    d['price'] = price
    d['degree'] = degree
    return d

#*** Price ***
def dict_create_price(drink_id, bar_id, price):
    d = dict()
    d['drink_id'] = drink_id
    d['bar_id'] = bar_id
    d['price'] = price
    return d

def dict_modify_price(price):
    d = dict()
    d['price'] = price
    return d