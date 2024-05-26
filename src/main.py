
from modules.workflow_config import WorkflowConfiguration

def main():
    workflow_config = WorkflowConfiguration()
    workflows = workflow_config.get_workflows()
    print("workflow", workflows)

if __name__ == "__main__":
    main()