from queues.observable_queue import ObservableQueue
from generators.leads_generator import simulate_lead_generation
from processors.lead_processor import LeadProcessor

import sys


def main(num_of_leads):
    print("Initializing LeadQueue...")
    
    leadProcessor = LeadProcessor()
    
    leadQueue = ObservableQueue()
    leadQueue.subscribe(leadProcessor.process_lead)

    print("Initialization of LeadQueue Completed.")
    for lead in simulate_lead_generation(num_of_leads):
        leadQueue.put(lead)



if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage : python main.py <number_of_leads_to_generate>")
        sys.exit(1)
    
    # Access the arguments
    num_of_leads = int(sys.argv[1])

    main(num_of_leads)