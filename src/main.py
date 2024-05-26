from queues.lead_queue import LeadQueue
from generators.leads_generator import simulate_lead_generation
from processors.lead_processor import LeadProcessor


def main():
    print("Initializing LeadQueue...")
    
    leadProcessor = LeadProcessor()
    
    leadQueue = LeadQueue()
    leadQueue.subscribe(leadProcessor.process_lead)

    print("Initialization of LeadQueue Completed.")
    for lead in simulate_lead_generation(20):
        leadQueue.put(lead)



if __name__ == "__main__":
    main()