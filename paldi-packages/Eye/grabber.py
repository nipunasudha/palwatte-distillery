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
import threading


#NOT USED