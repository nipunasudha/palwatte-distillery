import sys
import cv2

sys.path.insert(0, '/media/nipuna/APPS & GAMES/learn-opencv')
import areaSelector as AS
from tornado.ioloop import IOLoop


def parse_command(request,cam):
    cmd = request.form['cmd']
    data = request.form.getlist('data[]')
    commander(cmd, data)


def commander(cmd, data):
    if cmd == "EXIT":
        IOLoop.instance().stop()

    elif cmd == "PRINT":
        print("Ok, printed")
    elif cmd == "CROP":
        img = cv2.imread("rec.png")
        print(AS.getSelectionsFromImage(img))
