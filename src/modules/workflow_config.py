
from modules.generators import workflows_generator

class WorkflowConfiguration():

    def __init__(self):
        self.workflows = workflows_generator.generate_workflows(10)

    def get_workflows(self):
        return self.workflows