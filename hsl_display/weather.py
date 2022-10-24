import json
import requests
import time

from constants import KEYS


def query_weather_api(lat, lon):
	'''
	Sends a post request to OpenWeatheMaps Api.
	Parameters:

	lat (str): OWM location identifier.
	long (str): OWM location identifier.
	KEYS['OWM_KEY'](dict): OMW API key

	Returns:

	response (str): The response from the request
	'''

	url = "https://api.openweathermap.org/data/2.5/weather?lat="+ lat +"&lon="+ lon +"&appid="+ KEYS['OWM_KEY'] + ""
	payload = {"query":'{\n  "weather": {'}
	headers = {"Content-Type" : "application/json"}
	response = requests.get(url, headers=headers, data = json.dumps(payload))
	global dumped_weather
	dumped_weather = response.json()
	sort_weather()


def sort_weather():
	'''
	Sort the weather results to get only the last temperature.

	Parameters:

	last_temp (dict): Dictionary of the OWM API response.

	'''
	global last_temp
	last_weather = dumped_weather
	last_main = last_weather['main']
	last_temp = last_main['temp']
	convert_weather()


def convert_weather():
	'''
	Convert the last temperature from Kelvin to Celsius.

	Parameters:

	last_temp (float): Last temperature value.

	Returns:

	temp_in_int(int): Last temperature in Celsius
	'''

	global temp_in_int
	converted_temperature = last_temp - 273.15
	temp_in_int = int(converted_temperature)
	current_weather()	


def current_weather():

	degree_sign = u"\N{DEGREE SIGN}"
	global weather_now
	weather_now = str(temp_in_int) + "C" + degree_sign
	return weather_now


def current_time():
	global time_now
	time_now = time.strftime('%H %M', time.localtime(time.time()))
	return time_now	
