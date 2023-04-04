from bus import query_stop_api
from constants import KEYS
from flask import Flask, json, render_template
from weather import query_weather_api

app = Flask(__name__)


class Bus:
    def __init__(self, info):
        self.info = info


@app.route("/")
def start_serv():

    query_stop_api(KEYS['STOP_1'])
    query_weather_api(KEYS['LAT'], KEYS['LON'])
    from bus import bus_order
    from weather import current_time, current_weather
    busses = []
    for i in range(0, 5):
        b1 = Bus(bus_order(i))
        busses.append(b1.info)
    try:
        return render_template('index.html',
                               timen=current_time(),
                               weathern=current_weather(),
                               busComplete=busses)

    except NameError:
        return render_template('index.html',
                               timen=current_time(),
                               weathern=current_weather())


if __name__ == "__main__":
    app.run(debug=True)
