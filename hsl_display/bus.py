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
	return dumped_data


class Bus:
	def __init__(self, number, name, time):
		self.number = number
		self.name = name
		self.time = time

def bus_order (number):
	'''
	Access the API query response to the level of 'shortName' / bus number

	Parameters:

	number(int): The number of the bus in the API query response
	bus_short_name(int): HSL bus number.

	Returns:

	response (str): The bus number
	'''
	data_wrap = dumped_data['data']
	stop_wrap = data_wrap['stop']
	stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']

	global bus_short_name
	bus_short_name = stop_times_wrap[number]['trip']['route']['shortName']

	global bus_headsign
	bus_headsign = stop_times_wrap[number]['headsign']

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
	return bus_short_name, bus_headsign, norm_left 
