import time
import random

from utils.settings import load_settings
from utils.logger import get_logger

class LeadProcessor():
    """
    Processor that process each lead.
    """
    
    def __init__(self):
        """
        Initialises LeadProcessor by loading workflows mappings from settings.
        It also initialises logger.
        """
        settings = load_settings()
        self.workflows_mappings = settings.get('workflows_mapping',[])
        self.logger = get_logger()

    def process_lead(self,lead):
        """
        This function processes each lead.
        """
        lead_source = lead['source']

        time.sleep(random.uniform(0.1, 2.0))
        message = "Lead received from " + str(lead_source) + ". Processed with " + str(self.workflows_mappings.get(lead_source,{})['persona']) + " and sent by " + str(self.workflows_mappings.get(lead_source,{})['output_channel']) + " communication channel."
        print(message)
        self.logger.info(message)
