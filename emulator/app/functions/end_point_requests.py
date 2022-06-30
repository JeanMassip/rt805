from .crud_requests import *

# *** Sign ***
def sign_in_request(payload):
    send_post_request("/api/users/sign-in", payload)

def sign_out_request():
    send_get_request("/api/users/sign-out")

def sign_up_request(payload):
    send_post_request("/api/users/register", payload)

#*** Activity ***

def create_activity_request(payload):
    send_post_request("/api/activities", payload)

def get_all_activities_by_user(user_id):
    return send_get_request("/api/user/{}/activities".format(user_id))

def get_activity_data_by_activity(activity_id):
    return send_get_request("/api/activities/{}".format(activity_id))

def get_all_steps_by_activity(activity_id):
    return send_get_request("/api/activities/{}/steps".format(activity_id))

def modify_activity_request(activity_id, payload):
    send_put_request("/api/activities/{}".format(activity_id), payload)

def remove_activity(activity_id):
    send_delete_request("/api/activities/{}".format(activity_id))

#*** Steps ***
def create_step(payload):
    send_post_request("/api/steps", payload)

def get_step_data_by_step(step_id):
    return send_get_request("/api/steps/{}".format(step_id))

def get_all_consumptions_by_step(step_id):
    return send_get_request("/api/steps/{}/consumptions".format(step_id))

def get_bar_data_by_step(step_id):
    return send_get_request("/api/steps/{}/bar".format(step_id))

def remove_step(step_id):
    send_delete_request("/api/activities/{}".format(step_id))

#*** Consumptions **
def create_consumption(payload):
    send_post_request("/api/consumptions", payload)

def get_consumption_data_by_consumption(consumption_id):
    return send_get_request("/api/consumptions/{}".format(consumption_id))

def remove_consumption(consumption_id):
    send_delete_request("/api/consumptions/{}".format(consumption_id))

#*** Bar ***
def create_bar(payload):
    send_post_request("/api/bar", payload)

def get_all_bars():
    return send_get_request("/api/bars")

def get_bar_data_by_bar(bar_id):
    return send_get_request("/api/bar/{}".format(bar_id))

def remove_bar(bar_id):
    send_delete_request("/api/bar/{}".format(bar_id))

#*** Drink ***
def create_drink(payload):
    send_post_request("/api/drink", payload)

def get_all_drinks():
    return send_get_request("/api/drink")

def get_drink_data_by_drink(drink_id):
    return send_get_request("/api/drink/{}".format(drink_id))

def remove_drink(drink_id):
    send_delete_request("/api/drink/{}".format(drink_id))

#*** Price ***
def create_price(payload):
    send_post_request("/api/price", payload)

def get_all_prices():
    return send_get_request("/api/prices")

def get_price_data_by_price(price_id):
    return send_get_request("/api/price/{}".format(price_id))

def modify_price(price_id, payload):
    send_put_request("/api/price/{}".format(price_id))

def remove_price(price_id):
    send_delete_request("/api/price/{}".format(price_id))