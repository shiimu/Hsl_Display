from flask import Flask, render_template, json, jsonify
import time
import requests

from constants import COORDS, STOP_ID

from bus import query_stop_api
from weather import query_weather_api

app = Flask(__name__)


class Bus:
	def __init__(self, number):
		self.number = number



@app.route("/")
def start_serv():

	query_stop_api(STOP_ID['STOP_1'])
	query_weather_api(COORDS['LAT'], COORDS['LON'])
	from weather import current_weather, current_time
	from bus import bus_order
	busses = []
	for i in range(0, 5):
		b1 = Bus(bus_order(i))
		busses.append(b1.number)
	return render_template('index.html', timen = current_time(), weathern = current_weather(), busComplete = busses)

# except: return render_template('index.html', timen = timeNow, weathern = weatherNow)

if __name__ == "__main__":
	app.run(debug=True)
