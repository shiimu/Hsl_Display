import requests
import json


def queryApi(stop_id):
    url = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    payload = {"query": "{\n  stop(id: \"" + stop_id +
               "\") {  name   stoptimesWithoutPatterns{realtimeDeparture    serviceDay   headsign trip{route{ shortName}}}}}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))

    dumped_data = response.json()
    print(dumped_data)
