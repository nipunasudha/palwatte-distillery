from flask import Flask, request, jsonify
from flask_cors import CORS
# Tornado serving utility
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# Import image processor
import image_processor as im
import os
import pprint
import json
import server_tools as st

cwd = os.getcwd()
cam = im.init_camera(0)
requestCount = 0
app = Flask(__name__)
CORS(app)
print("Initiated.")


# RECIEVING POST REQUEST
@app.route('/post', methods=['POST'])
def resultp():
    global requestCount
    st.parse_command(request)
    requestCount += 1
    return json.dumps(
        {'data': [requestCount],
         'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'fake.png')})


http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
