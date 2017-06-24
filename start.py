import set_paths
import os
import Router.router_dispatch as dispatcher

relPath = ""
if os.name == "nt":
    relPath = os.path.join(set_paths.path[2], 'run_server.py')
else:
    print("Please change shell command for linux")
dispatcher.run_server(relPath)