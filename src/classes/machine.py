import json

class Machine:

    def __init__(self):
         
        with open('./machine.config') as json_file:  
            self.machines = json.load(json_file) 

