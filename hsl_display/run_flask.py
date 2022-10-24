from flask import Flask, render_template, json, jsonify
import time
import requests

from constants import COORDS, STOP_ID

from bus import query_stop_api
from weather import query_weather_api

app = Flask(__name__)


query_stop_api(STOP_ID['STOP_1'])
query_weather_api(COORDS['LAT'], COORDS['LON'])

@app.route("/")
def start_serv():

    query_stop_api(STOP_ID['STOP_1'])
    query_weather_api(COORDS['LAT'], COORDS['LON'])
    from weather import current_weather, current_time
    from bus import  bus_number, bus_name, bus_time_left, refresh_data

    current_weather()
    current_time()
    refresh_data()

    return render_template('index.html', timen = current_time(), weathern = current_weather(), busName = bus_name(0), busNumber = bus_number(0), normLeft = bus_time_left(0))

# except: return render_template('index.html', timen = timeNow, weathern = weatherNow)

if __name__ == "__main__":
    app.run(debug=True)
