import csv
import json

def requestedData(value,return_id):
    filepath = f'./data/JSON/{value}.json'
    with open(filepath) as f:
        data = json.load(f);
    if return_id is None:
        return data
    return data[return_id]





