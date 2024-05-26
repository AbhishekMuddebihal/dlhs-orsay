from queues.observable_queue import ObservableQueue
from generators.leads_generator import simulate_lead_generation
from processors.lead_processor import LeadProcessor


def main():
    print("Initializing LeadQueue...")
    
    leadProcessor = LeadProcessor()
    
    leadQueue = ObservableQueue()
    leadQueue.subscribe(leadProcessor.process_lead)

    print("Initialization of LeadQueue Completed.")
    for lead in simulate_lead_generation(20):
        leadQueue.put(lead)



if __name__ == "__main__":
    main()