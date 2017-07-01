from flask import Flask, request, jsonify, render_template, Response, redirect
from flask_cors import CORS
# Import image processor
import image_processor as imp
from Eye.init_camera import VideoCamera
from Utilities import rule_manager as rm
import os
import json
import server_tools as st
import pprint
import areaSelector as AS

cam = 1
crop_coords = [(71, 144), (306, 228), (333, 143), (565, 226), (67, 246), (310, 328), (331, 243), (567, 330)]
cwd = os.getcwd()
requestCount = 0
app = Flask(__name__)
CORS(app)
print("Initiated.")


# RECIEVING GET REQUEST
@app.route('/get-rules', methods=['GET'])
def get_rules():
    return json.dumps(
        {
            'data': rm.ruleData
        })


# RECIEVING GET REQUEST
@app.route('/get-ocr', methods=['GET'])
def get_ocr():
    global cam, crop_coords

    if validateCamera():
        command_result = st.commander("OCR", None, cam)
        command_result[0] = crop_coords
        print(command_result[0])
        detected_text = imp.start_processing(command_result)
        if isinstance(detected_text, list):
            pprint.pprint(detected_text)
        return json.dumps(
            {'detected_text': detected_text})
    else:
        return json.dumps(
            {
                'myerror': ["Camera is not availabe (ocr)"]
            })


@app.route('/post', methods=['POST'])
def resultp():
    global requestCount, cam

    if validateCamera():
        command_result = st.parse_command(request, cam)
        print(command_result[0])
        detected_text = imp.start_processing(command_result)
        if isinstance(detected_text, list):
            pprint.pprint(detected_text)
        requestCount += 1
        return json.dumps(
            {'data': [requestCount],
             'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'fake.png')})
    else:
        print('Camera is not started yet')
        return Response("No camera!",
                        mimetype='multipart/x-mixed-replace; boundary=frame')


def ocr_camera():
    global cam
    if validateCamera():
        img = cam.get_frame_for_cv()
        command_result = [AS.getSelectionsFromImage(img), img]
        print(command_result[0])
        detected_text = imp.start_processing(command_result)
        if isinstance(detected_text, list):
            pprint.pprint(detected_text)


@app.route('/post-generic', methods=['POST'])
def generic_post():
    rm.add_rule(request)
    return redirect("http://localhost:8000/rules", code=302)


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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
