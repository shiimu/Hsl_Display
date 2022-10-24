import requests
import json
import time
import os

from constants import KEYS


def query_stop_api(stop_id):
	'''
	Sends a post request to Digitransit Api.
	Parameters:

	stop_id(str): HSL bus stop id.

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


def bus_number (number):
	'''
	Access the API query response to the level of 'shortName' / bus number

	Parameters:

	number(int): The number of the bus in the API query response
	bus_short_name(int): HSL bus number.

	Returns:

	response (str): The bus number
	'''

	global bus_short_name
	bus_short_name = stop_times_wrap[number]['trip']['route']['shortName']
	return bus_short_name


def bus_name(number):
	'''
	Access the API query response to the level of 'headsign'.

	Parameters:

	number(int): The number of the bus in the API query response
	bus_headsign(str): HSL bus headsign.

	Returns:

	response (str): returns the bus's headsign
	'''

	global bus_headsign
	bus_headsign = stop_times_wrap[number]['headsign']
	return bus_headsign


def bus_time_left(number):
	'''
	Sends a post request to Digitransit Api.
	Parameters:

	number(int): The number of the bus in the API query response
	stop_id(str): HSL bus stop id.
	norm_left(datetime): Time until departure

	Returns:

	response (datetime):  Return the minutes left for this hour
	or the time if it is coming in over an hour.
	'''
	global norm_left

	# Access departure time
	stop_day = int(stop_times_wrap[number]['serviceDay'])
	stop_time= int(stop_times_wrap[number]['realtimeDeparture'])

	# Calculate the time left until departure
	bus_time = stop_day + stop_time
	current_time = time.time()
	time_left = bus_time - int(current_time)
	norm_left = time.strftime('%M', time.localtime(time_left))

	if time_left > 3600:
		norm_left = time.strftime('%H:%M', time.localtime(bus_time))
		return norm_left
	elif time_left < 0:
		norm_left = '00'
		return norm_left
	return norm_left


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


def bus_complete(number):
	bus_number(number)
	bus_name(number)
	bus_time_left(number)
	return
