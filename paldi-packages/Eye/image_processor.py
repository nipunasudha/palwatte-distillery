import numpy as np
import cv2
import os


def init_camera(id=0):
    cap = cv2.VideoCapture(id)
    # cap.set(3, 320)  # these are optional
    # cap.set(4, 240)
    return cap


def release_camera(cap):
    cap.release()


def read_camera(cap, path=""):
    # def read_camera(cap, path="/media/nipuna/APPS & GAMES/lumino/web/img/photoFromCam.jpg"):
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, frame)
    print('Saved.')
