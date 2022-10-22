import requests
import json

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
	print(dumped_data)


data_wrap = []


# def refresh_data():
	# global data_wrap
	# global stop_times_wrap
	# global dumped_data
	# # data_wrap.clear()
	# filesize = os.path.getsize("datadump.json")
	# try:
		# with open('datadump.json') as f:
		# dumped_data = json.load(f)
		# data_wrap = dumped_data['data']
		# stop_wrap = data_wrap['stop']
		# stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
		# return data_wrap
	# except filesize == 0:
		# print('Error! datadump.json is empty')


# def sortBus(number):
	# global bus_name
	# global norm_left
	# global bus_number
