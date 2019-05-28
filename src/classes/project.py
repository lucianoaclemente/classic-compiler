# coding: utf-8
import os
import json
from classes.machine import Machine
from classes.common import Common

class Project:
    
     def __init__(self):
         
        with open(os.path.join(Common.params["project_path"], 'project.config')) as json_file:  
            self.config = json.load(json_file) 
			
            machine = Machine()
			
            self.machine = machine.machines[self.config["machine"]]
