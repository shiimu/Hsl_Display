import json
import requests

secret = {
	"owm":"fcc250fd2a7a605c8269de49d1dc6dda"
	}

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

	url = "https://api.openweathermap.org/data/2.5/weather?lat="+ lat +"&lon="+ lon +"&appid="+ secret['owm'] + ""
	payload = {"query":'{\n  "weather": {'}
	headers = {"Content-Type" : "application/json"}
	response = requests.get(url, headers=headers, data = json.dumps(payload))
	global dumped_weather
	dumped_weather = response.json()
	sortWeather()

	
def sortWeather():
	global last_temp
	last_weather = dumped_weather
	last_main = last_weather['main']
	last_temp = last_main['temp']
	convertWeather()


def convertWeather():
	global temp_in_int
	converted_temperature = last_temp - 273.15
	temp_in_int = int(converted_temperature)
