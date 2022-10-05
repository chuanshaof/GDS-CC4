from urllib.request import urlopen
import json, sys, csv

def main():
    # https://stackoverflow.com/questions/71459981/how-to-solved-charmap-codec-cant-encode-character-u300b
    sys.stdout.reconfigure(encoding='utf-8')

    # Change url here to what is necessary
    url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

    # https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
    with urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))

    print(len(data[0]["restaurants"]))
    print(data[0]["restaurants"][0]["restaurant"]["R"]["res_id"])
    print(data[0]["restaurants"][0]["restaurant"]["name"])
    print(data[0]["restaurants"][0]["restaurant"]["location"]["country_id"])
    print(data[0]["restaurants"][0]["restaurant"]["location"]["city"])
    print(data[0]["restaurants"][0]["restaurant"]["user_rating"]["aggregate_rating"])
    print(data[0]["restaurants"][0]["restaurant"]["cuisines"])

    # https://docs.python.org/3/library/csv.html
    with open('task1.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')

        # Write the header of the file
        writer.writerow(["res_id", "name", "country_id", "city", "aggregate_rating", "cuisines"])

        writer.writerows(data) 


if __name__ == "__main__":
    main()
    