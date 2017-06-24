import sys

sys.path.insert(0, '/media/nipuna/APPS & GAMES/learn-opencv')
import areaSelector as AS
from tornado.ioloop import IOLoop


def parse_command(request, cam):
    cmd = request.form['cmd']
    data = request.form.getlist('data[]')
    result = commander(cmd, data, cam)
    return result


def commander(cmd, data, cam):
    if cmd == "EXIT":
        IOLoop.instance().stop()

    elif cmd == "PRINT":
        print("Ok, printed")
    elif cmd == "CROP":
        img = cam.get_frame_for_cv()
        return [AS.getSelectionsFromImage(img),img]
