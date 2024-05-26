
from modules.workflow_config import WorkflowConfiguration

def main():
    workflow_config = WorkflowConfiguration()
    workflows_mappings = workflow_config.get_workflows_mappings()
    print("workflows mappings :", workflows_mappings)

if __name__ == "__main__":
    main()