from flask import Flask
from flask import jsonify
import requests
import re
app = Flask(__name__)

expr = r'@(?P<lat>([0-9]+.[0-9]+)),(?P<lng>([0-9]+.[0-9]+))'

@app.route('/api/<place>')
def findplace(place):
    place = place.replace(' ','+')
    response = requests.get('https://www.google.com/maps/place/'+place)
    if re.search(expr,response.text):
        m = re.search(expr,response.text)
        return jsonify({"status":"OK","lat":m.group('lat'),"lng":m.group('lng')}),200
    else:
        return jsonify({"status":"ZERO_RESULTS"}),200