import json
import os

from classes.common import Common

class Machine:

    def __init__(self):
    
        with open(os.path.join(Common.params["root_path"], 'machine.config')) as json_file:  
            self.machines = json.load(json_file) 

