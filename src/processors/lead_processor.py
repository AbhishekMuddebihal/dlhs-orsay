import time
import random
import os

from utils.settings import load_settings
from utils.logger import get_logger
from utils import file_utils

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

        self.json_store_filepath = os.path.join(os.path.dirname(__file__), '../../output/processed_event_store.json')
        
        # Deleting previously generated file
        file_utils.delete_file_if_exists(self.json_store_filepath)

        # Creating empty file to ensure its existance
        file_utils.create_file_if_not_exists(self.json_store_filepath)

    def process_lead(self,lead):
        """
        This function processes each lead.
        """
        lead_source = lead['source']

        time.sleep(random.uniform(0.1, 2.0))
        message = "Lead received from " + str(lead_source) + ". Processed with " + str(self.workflows_mappings.get(lead_source,{})['persona']) + " and sent by " + str(self.workflows_mappings.get(lead_source,{})['output_channel']) + " communication channel."
        print(message)
        self.logger.info(message)
        self.store_lead_process(lead, self.workflows_mappings.get(lead_source,{}), "success")

    def store_lead_process(self, lead, workflow, status):
        """
        Store lead processing status to json file.
        """
        lead['workflow'] = workflow
        lead['processing_status'] = status
        file_utils.append_to_json_file(self.json_store_filepath, lead)

