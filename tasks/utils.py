import csv, json, sys
from urllib.request import urlopen

# sys.stdin and sys.stdout for 'utf-8' such that it can read and write non-utf-8 characters
# https://stackoverflow.com/questions/71459981/how-to-solved-charmap-codec-cant-encode-character-u300b
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Change to other locations if needed
url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
file = "inputs/restaurant_data.json"


# Write to a CSV using a list of list
# Remember to edit missing data into "NA"
# https://docs.python.org/3/library/csv.html
def writeToCSV(filename: str, header: list[str], data: list[list]):
    with open(filename, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(header)
        writer.writerows(data) 

# ----------------- Reading JSON file -----------------
# https://pythonbasics.org/pandas-json/
# Accepts both URL And local file
def getJsonPd(source: str) -> dict:
    import pandas as pd
    df = pd.read_json(source)
    return df.to_dict()

# https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
def getJsonURL(url: str) -> dict:
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

# Accepts only local file
def getJsonLocal(filename: str) -> dict:
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)



