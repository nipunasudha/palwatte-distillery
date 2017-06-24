import os
import sys

path = ['', '', '', '']
path[0] = os.path.join(os.path.dirname(__file__), 'paldi-packages')
path[1] = os.path.join(os.path.dirname(__file__), 'paldi-packages', 'Eye')
path[2] = os.path.join(os.path.dirname(__file__), 'paldi-packages', 'Router')
path[3] = os.path.join(os.path.dirname(__file__), 'paldi-packages', 'Utilities')

for p in path:
    if p not in sys.path:
        sys.path.insert(1, p)
