import time
import json
import os

data_wrap = []


def refresh_data():
    global data_wrap
    global stop_times_wrap
    global dumped_data
    # data_wrap.clear()
    filesize = os.path.getsize("datadump.json")
    try:
        with open('datadump.json') as f:
            dumped_data = json.load(f)
            data_wrap = dumped_data['data']
            stop_wrap = data_wrap['stop']
            stop_times_wrap = stop_wrap['stoptimesWithoutPatterns']
            return data_wrap
    except filesize == 0:
        print('Error! datadump.json is empty')


def sort(number):
    global bus_name
    global norm_left
    global bus_number
