import os
import sys
import numpy as np
import PIL
from PIL import Image
import pyocr
import cv2
import pyocr.builders


# rectangle locations
# [(71, 144), (306, 228), (333, 143), (565, 226), (67, 246), (310, 328), (331, 243), (567, 330)]

# OCR initialization example with pyOCR
def initTool():
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool_ = tools[0]
    print("Will use tool '%s'" % (tool_.get_name()))
    langs = tool_.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[2]
    print("Will use lang '%s'" % (lang))
    return tool_


def start_processing(img_cropped):
    if isinstance(img_cropped, list): img_cropped = img_cropped[1]
    # ============================= TWO (pure red char on black)================================
    img_cropped = img_cropped[246:328, 67:310].copy()
    img_cropped=preprocess(img_cropped)
    read_digits(img_cropped)
    cv2.imshow("Cropped", img_cropped)
    cv2.waitKey()


def preprocess(img_cropped):
    img_cropped = cv2.medianBlur(img_cropped, 5)
    # img_cropped = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_cropped = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([15, 255, 255])

    img_cropped = cv2.inRange(img_cropped, lower_red, upper_red)

    img_cropped = cv2.bitwise_not(img_cropped)
    # ------------------------
    kernel = np.ones((4, 4), np.uint8)  # building a kernel, a unit of operation
    # --------------------------------
    img_cropped = cv2.morphologyEx(img_cropped, cv2.MORPH_CLOSE, kernel)
    img_cropped = cv2.morphologyEx(img_cropped, cv2.MORPH_OPEN, kernel)

    img_cropped = cv2.erode(img_cropped, kernel, iterations=4)
    img_cropped = cv2.dilate(img_cropped, kernel, iterations=3)
    # ------------------------
    return img_cropped


def read_digits(img_cropped):
    global tool
    digits = tool.image_to_string(
        Image.fromarray(img_cropped),
        lang="seg",
        builder=pyocr.tesseract.DigitBuilder()
    )
    print(digits)
    return digits


print("Image Processor Started")
tool = initTool()

# uncomment to capture fake images
# img = cv2.imread("four_panal.png", 1)
# start_processing(img)
