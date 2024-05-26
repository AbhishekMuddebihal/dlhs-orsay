
from modules.generators import workflows_generator
import json
import os

class WorkflowConfiguration():

    def __init__(self):
        self.workflows = []
        
        settings_path = os.path.join(os.path.dirname(__file__), '../configurations/settings.json')
        with open(settings_path,'r') as json_file:
            settings = json.load(json_file)
            self.workflows = settings['workflows_mapping']
    

    def get_workflows(self):
        return self.workflows