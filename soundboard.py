#!/usr/bin/python3

from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from flask import json
from pythonosc import udp_client
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route("/playback", methods=['POST'])
@cross_origin()
def sound_play():
	board = request.form['board']
	id = request.form['id']

	board_location = '/castersoundboard/board/' + str(board) + '/player/' + str(id) + '/modify/play_state/play'
	client = udp_client.SimpleUDPClient('127.0.0.1', 5051)
	client.send_message(board_location, 1)
	return ""



#if __name__ == '__main__':
#	app.run(host = '0.0.0.0',port=5000)

