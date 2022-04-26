
from datetime import datetime
import json


def entryEnter():
    with open('data.json', 'r') as f:
        data = json.load(f)
        for d in data:
            print("d['time']------->",d['time'])
            time = datetime.strptime(d['time'], "%Y-%m-%d %I:%M:%S"),
            print(time)
    return None


entryEnter()
