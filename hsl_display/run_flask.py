from flask import Flask, render_template, json, jsonify
import time
import requests

from bus import queryStopApi
from weather import queryWeatherApi

app = Flask(__name__)


degree_sign = u"\N{DEGREE SIGN}"

stop_id = 'HSL:1472113'
lat = '60.23787364561019'
lon = '25.10560957759351'

queryStopApi(stop_id)
queryWeatherApi(lat, lon)


@app.route("/")
def start_serv():
	timeNow = time.strftime('%H %M', time.localtime(time.time()))

	from weather import temp_in_int
	weatherNow = str(temp_in_int) + "C" + degree_sign

	from bus import  bus_number, bus_name, bus_time_left, refresh_data
	refresh_data()
	return render_template('index.html', timen = timeNow, weathern = weatherNow, busName = bus_name(0), busNumber = bus_number(0), normLeft = bus_time_left(0))

	# except: return render_template('index.html', timen = timeNow, weathern = weatherNow)

if __name__ == "__main__":
	app.run(debug=True)
