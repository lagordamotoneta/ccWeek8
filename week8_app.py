from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import requests
from pprint import pprint
import requests_cache

requests_cache.install_cache( 'air_api_cache' , backend= 'sqlite' , expire_after=360000)

app = Flask(__name__)

air_url_template = 'https://api.breezometer.com/air-quality/v2/historical/hourly?lat={lat}&lon={lng}&key={API_KEY}&start_datetime={start}&end_datetime={end}'
MY_API_KEY = '58b320b8f7304030977662a98fecd08f'

@app.route( '/airqualitychart' , methods=['GET'])
def airchart():
    my_latitude = request.args.get('lat','51.52369')
    my_longitude = request.args.get('lng' , '-0.0395857')
    my_start = request.args.get('start', '2019-02-24T07:00:00Z')
    my_end = request.args.get( 'end' , '2019-02-25T07:00:00Z' )
    air_url = air_url_template.format(lat=my_latitude, lng=my_longitude,API_KEY=MY_API_KEY, start=my_start, end=my_end)
    resp = requests.get(air_url)
    if resp.ok:
        resp = requests.get(air_url)
        pprint(resp.json())
    else:
        print(resp.reason)

    return ("Done!")

if __name__=="__main__":
    app.run(port=8080, debug=True)
