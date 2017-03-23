from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
# Tornado serving utility
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
# Import image processor
import image_processor as im
from Eye.init_camera import VideoCamera
import os
import pprint
import json
import server_tools as st

cwd = os.getcwd()
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


@app.route('/fun')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame != "error":
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


#
# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5000)
# IOLoop.instance().start()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
