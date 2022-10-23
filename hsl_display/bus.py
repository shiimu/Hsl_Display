import requests
import json
import time
import os

global secret
secret = {
    "hsl": "aa",
}

def queryStopApi(stop_id):
    '''
    Sends a post request to Digitransit Api.
    Parameters:

        stop_id(str): HSL bus stop id.
        secret['hsl'](dict): Digitransit API key

    Returns:

    response (str): The response from the request
    '''

    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    payload = {"query": "{\n  stop(id: \"" + stop_id +
               "\") {  name   stoptimesWithoutPatterns{realtimeDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    global dumped_data
    dumped_data = response.json()
    with open('datadump.json', 'w')as json_file:
        json.dump(dumped_data, json_file)

data_wrap = []

def refresh_data():
    global data_wrap
    global stop_times_wrap
    global dumped_data
    # data_wrap.clear()
    filesize = os.path.getsize("datadump.json")
    with open('datadump.json') as f:
        dumped_data = json.load(f)
        data_wrap = dumped_data['data']
        stop_wrap = data_wrap['stop']
        stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
        return data_wrap

def bus_name(number):
    '''
    Sends a post request to Digitransit Api.
    Parameters:

        stop_id(str): HSL bus stop id.
        secret['hsl'](dict): Digitransit API key

    Returns:

    response (str): The response from the request
    '''

    global bus_name
    bus_name = stop_times_wrap[number]['headsign']
    return bus_name
def bus_time_left(number):
    '''
    Sends a post request to Digitransit Api.
    Parameters:

        stop_id(str): HSL bus stop id.
        secret['hsl'](dict): Digitransit API key

    Returns:

    response (str): The response from the request
    '''
    global norm_left
    # Getting the departure time
    stop_day = int(stop_times_wrap[number]['serviceDay'])
    stop_time= int(stop_times_wrap[number]['realtimeDeparture'])

    bus_time = stop_day + stop_time
    current_time = time.time()
    time_left = bus_time - int(current_time)
    # throws an error if time_left is negative
    # print(time_left)
    norm_left = time.strftime('%M', time.localtime(time_left))
    if time_left > 3600:
        norm_left = time.strftime('%H:%M', time.localtime(bus_time))
        return norm_left
    elif time_left < 0:
        norm_left = '00'
        return norm_left
    return norm_left
def bus_number (number):
    '''
    Sends a post request to Digitransit Api.
    Parameters:

        stop_id(str): HSL bus stop id.
        secret['hsl'](dict): Digitransit API key

    Returns:

    response (str): The response from the request
    '''

    global bus_number
    bus_number = stop_times_wrap[number]['trip']['route']['shortName']
