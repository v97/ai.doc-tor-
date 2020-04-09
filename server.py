from flask import Flask, request, make_response
import urllib
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
	req = request.get_json(silent=True, force=True)
	res = processRequest(req)

	res = json.dumps(res, indent=4)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json'
	return r

def processRequest(req):
	query_response = req["queryResult"]
	print(query_response)
	text = query_response.get('queryText', None)
	parametres = query_response.get('parameters', None)

	res = get_data()

	return res

def get_data():
	speech = "vsamba"

	return {
		"fulfillmentText": speech
	}

if __name__ == '__main__':
    app.run()