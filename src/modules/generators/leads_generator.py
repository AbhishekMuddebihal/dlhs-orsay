import random
import string
import time
from datetime import datetime
from utils.settings import load_settings

def generate_random_name():
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Michael', 'Sarah']
    last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email(name):
    domains = ['example.com', 'test.com', 'demo.com']
    return f"{name.replace(' ', '.').lower()}@{random.choice(domains)}"

def generate_random_phone():
    return ''.join(random.choices(string.digits, k=10))

def generate_random_lead_source():
    settings = load_settings()
    sources = settings.get('lead_sources', [])
    return random.choice(sources)

def generate_random_interest_level():
    levels = ['Low', 'Medium', 'High']
    return random.choice(levels)

def generate_lead():
    name = generate_random_name()
    lead = {
        'name': name,
        'email': generate_random_email(name),
        'phone': generate_random_phone(),
        'source': generate_random_lead_source(),
        'interest_level': generate_random_interest_level(),
        'timestamp': datetime.now().isoformat()
    }
    return lead

def simulate_lead_generation(num_leads):
    leads = []
    for _ in range(num_leads):
        leads.append(generate_lead())
        time.sleep(random.uniform(0.1, 1.0))  # Simulate time delay for lead input
    return leads