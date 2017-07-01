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
import cv2
import platform
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
            {
                'detected_text': detected_text,
                'mystatcode': "OCR-S",
                'mystat': "OCR Success."

            })
    else:
        return json.dumps(
            {
                'mystatcode': "OCR-D",
                'mystat': "Camera is not availabe for OCR."
            })


@app.route('/post', methods=['POST'])
def resultp():
    global requestCount, cam

    if validateCamera():
        # ----------------------------------------------
        rqcmd = request.form['cmd']
        rqdata = request.form.getlist('data[]')
        command_result = st.commander(rqcmd, rqdata, cam)
        # ----------------------------------------------
        if rqcmd == "CROP":
            if set_coordinates(command_result):

                return json.dumps(
                    {
                        'mystatcode': "CROP-S",
                        'mystat': "Region Selection Success.",
                        'coords': command_result[0]
                    })
            else:
                return json.dumps(
                    {
                        'mystatcode': "CROP-W",
                        'mystat': "Error! Can't set coordinates."
                    })

    else:
        print('Camera not valid')
        return json.dumps(
            {
                'mystatcode': "CAM-D",
                'mystat': "Can't access camera."
            })


def set_coordinates(command_result):
    global crop_coords
    coords = command_result[0]

    if isinstance(coords, list):
        crop_coords = coords
        pprint.pprint(coords)
        return True
    else:
        return False


# RECIEVING GET REQUEST
@app.route('/get-info', methods=['GET'])
def collect_system_info():
    global cam
    info = {}

    info['cam_stat'] = validateCamera()
    info['cam_width'] = "N/A"
    info['cam_height'] = "N/A"
    if validateCamera():
        width = cam.video.get(3)  # float
        height = cam.video.get(4)  # float
        info['cam_width'] = width
        info['cam_height'] = height

    info['plat_os'] = platform.platform()
    info['plat_bit'] = platform.machine()
    info['plat_proc'] = platform.processor()
    pprint.pprint(info)
    return json.dumps(info)


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
    collect_system_info()
    if validateCamera():
        return json.dumps(
            {
                'mystatcode': "CAM-I",
                'mystat': "Camera already ON."
            })
    else:
        cam = VideoCamera()
        return json.dumps(
            {
                'mystatcode': "CAM-S",
                'mystat': "Camera started!"
            })


@app.route('/stopcam')
def delVidObj():
    global cam
    collect_system_info()
    if validateCamera():
        del cam
        return json.dumps(
            {
                'mystatcode': "CAM-S",
                'mystat': "Camera stopped!"
            })
    else:
        print('Camera is not started yet')
        return json.dumps(
            {
                'mystatcode': "CAM-I",
                'mystat': "Camera already OFF"
            })


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
