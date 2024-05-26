import os
import json

def load_settings():
    settings_path = os.path.join(os.path.dirname(__file__), '../configurations/settings.json')
    settings = {}
    with open(settings_path,'r') as json_file:
        settings = json.load(json_file)
    return settings