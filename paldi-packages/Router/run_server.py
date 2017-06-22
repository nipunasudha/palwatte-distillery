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

testData = ["Nipuna", "Sudharaka", "Wijesinghe"]
ruleData = [
    {
        "variableID": "wow",
        "variableName": "wow",
        "minDangerValue": "wow",
        "minWarningValue": "wow",
        "maxWarningValue": "wow",
        "maxDangerValue": "wow"},
    {
        "variableID": "not so wow",
        "variableName": "not so wow",
        "minDangerValue": "not so wow",
        "minWarningValue": "not so wow",
        "maxWarningValue": "not so wow",
        "maxDangerValue": "not so wow"}

]
cam = 1
cwd = os.getcwd()
requestCount = 0
app = Flask(__name__)
CORS(app)
print("Initiated.")


# RECIEVING POST REQUEST
@app.route('/get-rules', methods=['GET'])
def get_rules():
    global testData
    return json.dumps(
        {
            'data': ruleData
        })


@app.route('/post', methods=['POST'])
def resultp():
    global requestCount, cam

    if validateCamera():
        st.parse_command(request, cam)
        requestCount += 1
        return json.dumps(
            {'data': [requestCount],
             'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'fake.png')})
    else:
        print('Camera is not started yet')
        return Response("No camera!",
                        mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/camera-stream')
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
    global cam
    if validateCamera():
        return Response(gen(cam),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        print('Camera is not started yet')
        return Response("No camera!",
                        mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/startcam')
def getVidObj():
    global cam
    if validateCamera():
        return Response("Camera is already ON!", mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        cam = VideoCamera()
        return Response({"data": "done"}, mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stopcam')
def delVidObj():
    global cam
    if validateCamera():
        del cam
    else:
        print('Camera is not started yet')
    return Response({"data": "done"}, mimetype='multipart/x-mixed-replace; boundary=frame')


def validateCamera():
    global cam
    try:
        cam
    except NameError:
        return False
    else:
        if cam == 1:
            return False
        else:
            return True


# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5000)
# IOLoop.instance().start()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
