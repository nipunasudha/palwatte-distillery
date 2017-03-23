import numpy as np
import cv2
import os


def release_camera(cap):
    cap.release()


def read_camera(cap, path=""):
    # def read_camera(cap, path="/media/nipuna/APPS & GAMES/lumino/web/img/photoFromCam.jpg"):
    ret, frame = cap.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, frame)
    print('Saved.')
