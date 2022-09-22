from flask import Flask, render_template, json, jsonify
import time
import requests

from query_api import queryApi

app = Flask(__name__)

stop_id = 'HSL:1472113'

queryApi(stop_id)


@app.route("/")
def start_serv():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
