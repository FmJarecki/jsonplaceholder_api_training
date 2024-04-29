import json

with open('config.json', 'r') as file:
    config_data = json.load(file)

API_KEY = config_data['API_KEY']
