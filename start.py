import set_path
import os
import Utilities.tools as tools
import Eye.image_processor as imp
import time
import Router.router_dispatch as dispatcher

# Prepare path & execute run_server.py
# relPath = ""
# if os.name == "nt":
#     relPath = os.path.join(set_path.path[2], 'run_server.py')
# else:
#     print("Please change shell command for linux")
# dispatcher.run_server(relPath)

# fake image processor

cam = imp.init_camera(0)
while True:
    start_time = time.time()
    imp.read_camera(cam)

    tools.time_regulator(2, start_time)
