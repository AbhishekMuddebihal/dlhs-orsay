import random

def generate_random_persona():
    personas = [
        "Sofia",
        "Liam",
        "Olivia",
        "Noah",
        "Emma",
        "Ava",
        "Mason",
        "Isabella",
        "Lucas",
        "Mia",
        "Ethan",
        "Amelia",
        "James",
        "Harper",
        "Alexander",
        "Evelyn",
        "Henry",
        "Aria",
        "Aiden",
        "Scarlett"
    ]
    return random.choice(personas)

def generate_random_output_channel():
    output_channels = [
        "Email",
        "SMS",
        "Phone Call",
        "Social Media Message",
        "WhatsApp"
    ]
    return random.choice(output_channels)

def generate_workflow():
    workflow = {
        'lead_source': None,
        'persona': generate_random_persona(),
        'output_channel': generate_random_output_channel()
    }
    return workflow

def generate_workflows(n_workflows):
    workflows = []
    for _ in range(n_workflows):
        workflows.append(generate_workflow())
    return workflows