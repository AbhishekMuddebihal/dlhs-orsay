
from utils.settings import load_settings
import json
import os

class WorkflowConfiguration():

    def __init__(self):
        settings = load_settings()

        self.workflows_mappings = settings['workflows_mapping']
    

    def get_workflows_mappings(self):
        return self.workflows_mappings