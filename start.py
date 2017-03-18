import set_path
import os
import Utilities.Config as Config
import Router.router_dispatch as dispatcher

relPath = ""
if os.name == "nt":
    relPath = os.path.join(set_path.path[2], 'run_server.py')
else:
    print("Please change shell command for linux")
dispatcher.run_server(relPath)

print(Config.read_settings())
