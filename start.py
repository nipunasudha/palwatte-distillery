import set_paths
import os
import Utilities.tools as tools
import Eye.image_processor as imp
import time
import Router.router_dispatch as dispatcher

# Prepare path & execute run_server.py
relPath = ""
if os.name == "nt":
    relPath = os.path.join(set_paths.path[2], 'run_server.py')
else:
    print("Please change shell command for linux")
dispatcher.run_server(relPath)

# fake image processor

# while True:
# start_time = time.time()
# output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web-app", "web", "img", "photoFromCam.jpg")
#
# imp.read_camera(cam, output_path)

# tools.time_regulator(0.6, start_time)
