import csv
import json

def requestedData(value):
    filepath = f'./data/JSON/{value}.json'
    with open(filepath) as f:
        data = json.load(f)
    return data







