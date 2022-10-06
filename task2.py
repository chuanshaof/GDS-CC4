from urllib.request import urlopen
import pandas as pd
import json, sys, csv

def main():
    # https://stackoverflow.com/questions/71459981/how-to-solved-charmap-codec-cant-encode-character-u300b
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    # ----------------- Reading JSON file -----------------
    # Change url here to what is necessary
    url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
    
    # # https://pythonbasics.org/pandas-json/
    # # 1. Reading json file using pandas
    # df = pd.read_json(url)
    # rawData = df.to_dict()

    # # 2. Read JSON file from local file directory
    # with open("restaurant_data_bugged.json", "r", encoding="utf-8") as f:
    #     rawData = json.load(f)
    
    # 3. Read JSON file from url
    # https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
    with urlopen(url) as response:
        rawData = json.loads(response.read().decode("utf-8"))
    
    events = []
    for data in rawData:
        for restaurant in data["restaurants"]:
            restaurant = restaurant["restaurant"]

            # Get id and name in advance
            restaurantId = restaurant.get("R", {}).get("res_id", "")
            restaurantName = restaurant.get("name", "")
            
            for event in restaurant.get("zomato_events", []):
                event = event["event"]
                eventId = event.get("event_id", "")
                eventTitle = event.get("title", "")
                eventStart = event.get("start_date", "")
                eventEnd = event.get("end_date", "")
                photoURLList = []

                for photo in event.get("photos", []):
                    photoURLList.append(photo.get("photo", {}).get("url", ""))
                
                events.append([eventId, restaurantId, restaurantName, photoURLList, eventTitle, eventStart, eventEnd])

    eventsDf = pd.DataFrame(events, columns=["event_id", "res_id", "res_name", "photos", "event_title", "start_date", "end_date"])
    eventsDf.replace("", "NA", inplace=True)
    eventsDf.to_csv("task2.csv", index=False)
    

    # restaurantsDf = pd.DataFrame(events, columns=["eventId", "name", "country", "city", "votes", "rating", "cuisines"])
    # restaurantsDf.replace("", "NA", inplace=True)
    # restaurantsDf.to_csv("task1.csv", index=False)

    # # Note that there may be multiple events
    # print(rawData[0]["restaurants"][0]["restaurant"]["zomato_events"][0]["event"]["event_id"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["id"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["name"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["zomato_events"][0]["event"]["photos"][0]["photo"]["url"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["zomato_events"][0]["event"]["title"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["zomato_events"][0]["event"]["start_date"])
    # print(rawData[0]["restaurants"][0]["restaurant"]["zomato_events"][0]["event"]["end_date"])

if __name__ == "__main__":
    main()