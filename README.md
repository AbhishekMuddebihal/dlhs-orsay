# Dynamic Lead Handling System Prototype

This project is a prototype for a Dynamic Lead Handling System designed for sales. The system generates leads, assigns workflows based on lead sources, personas, and output channels.

## Features

- Simulates lead generation with random attributes.
- Defines workflows based on lead source, persona, and output channel.
- Stores generated leads and workflows in JSON format.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbhishekMuddebihal/dlhs-orsay.git
    cd dlhs-orsay
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
    ```bash
    python main.py <number_of_leads_to_generate>
    ```

    This will generate leads and processes, and save status to output/processed_event_store.json.

## Lead Attributes

    - Name: Randomly generated name.
    - Email: Randomly generated email based on the name.
    - Phone: Randomly generated 10-digit phone number.
    - Lead Source: Randomly selected from predefined sources.
    - Interest Level: Randomly assigned interest level (Low, Medium, High).
    - Timestamp: Current timestamp of lead generation.

## Workflow Attributes

    - Lead Source: Randomly selected from predefined sources.
    - Persona: Randomly assigned persona.
    - Output Channel: Randomly selected from predefined channels.

## Example

    Here’s an example of a generated lead with an assigned workflow:

    ```
    {
        "name": "Sofia Smith",
        "email": "sofia.smith@example.com",
        "phone": "1234567890",
        "source": "Social Media",
        "interest_level": "High",
        "timestamp": "2024-05-26T12:34:56.789012",
        "workflow": {
            "persona": "Tech Enthusiast",
            "output_channel": "WhatsApp"
        }
    }
    ```





