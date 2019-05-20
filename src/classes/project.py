# coding: utf-8
import json
from classes.machine import Machine

class Project:
    
     def __init__(self, project_path):
         
        self.project_path = project_path
         
        with open(project_path + '/project.config') as json_file:  
            self.config = json.load(json_file) 
			
            machine = Machine()
			
            self.machine = machine.machines[self.config["machine"]]
