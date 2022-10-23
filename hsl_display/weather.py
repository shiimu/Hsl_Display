import json
import requests
from constants import keys

def queryWeatherApi(lat, lon):
	'''
	Sends a post request to OpenWeatheMaps Api.
	Parameters:

	lat (str): OWM location identifier.
	long (str): OWM location identifier.
	secret['owm'](dict): OMW API key

	Returns:

		response (str): The response from the request
	'''

	url = "https://api.openweathermap.org/data/2.5/weather?lat="+ lat +"&lon="+ lon +"&appid="+ keys['owm_key'] + ""
	payload = {"query":'{\n  "weather": {'}
	headers = {"Content-Type" : "application/json"}
	response = requests.get(url, headers=headers, data = json.dumps(payload))
	global dumped_weather
	dumped_weather = response.json()
	sortWeather()


def sortWeather():
	'''
	Sort the weather results to get only the last temperature.

	Parameters:

	last_temp (dict): Dictionary of the OWM API response.

	'''
	global last_temp
	last_weather = dumped_weather
	last_main = last_weather['main']
	last_temp = last_main['temp']
	convertWeather()


def convertWeather():
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
