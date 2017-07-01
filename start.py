import set_paths
import os
import Router.router_dispatch as dispatcher

relPathr = ""
relPathp = ""
if os.name == "nt":
    relPathr = os.path.join(set_paths.path[2], 'run_server.py')
    relPathp = os.path.join(set_paths.path[3], 'periodate.py')
else:
    print("Please change shell command for linux")
dispatcher.run_service(relPathr)
dispatcher.run_service(relPathp)
