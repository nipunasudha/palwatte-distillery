import sys

sys.path.insert(0, '/media/nipuna/APPS & GAMES/learn-opencv')
import areaSelector as AS
from tornado.ioloop import IOLoop
from Utilities import rule_manager as rm


def commander(cmd, data, cam):
    if cmd == "EXIT":
        IOLoop.instance().stop()
    elif cmd == "CROP":
        img = cam.get_frame_for_cv()
        return [AS.getSelectionsFromImage(img), img]
    elif cmd == "OCR":
        img = cam.get_frame_for_cv()
        return [None, img]
