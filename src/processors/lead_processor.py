from utils.settings import load_settings

class LeadProcessor():
    """
    Processor that process each lead.
    """
    
    def __init__(self):
        """
        Initialises LeadProcessor by loading workflows mappings from settings.
        """
        settings = load_settings()
        self.workflows_mappings = settings.get('workflows_mapping',[])

    def process_lead(self,lead):
        """
        This function processes each lead.
        """
        lead_source = lead['source']
        print("processing lead by",self.workflows_mappings.get(lead_source,{})['persona'])