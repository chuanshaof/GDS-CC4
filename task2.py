from urllib.request import urlopen
import pandas as pd
import json, sys, csv, datetime

def main():
    # https://stackoverflow.com/questions/71459981/how-to-solved-charmap-codec-cant-encode-character-u300b
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")

    # ----------------- Reading JSON file -----------------
    # Change url here to what is necessary
    url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"

    # Read JSON file from url
    # https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
    with urlopen(url) as response:
        rawData = json.loads(response.read().decode("utf-8"))

    # Reading date time
    # https://www.geeksforgeeks.org/converting-string-yyyy-mm-dd-into-datetime-in-python/
    dateTimeFormat = "%Y-%m-%d"

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

                dtEventStart = datetime.datetime.strptime(eventStart, dateTimeFormat)
                dtEventEnd = datetime.datetime.strptime(eventEnd, dateTimeFormat)

                apr1 = datetime.datetime(2019, 4, 1)
                apr30 = datetime.datetime(2019, 4, 30)

                if dtEventStart >= apr1 and dtEventStart <= apr30:
                    events.append([restaurantId, restaurantName, eventId, eventTitle, eventStart, eventEnd, photoURLList])
                elif dtEventEnd >= apr1 and dtEventEnd <= apr30:
                    events.append([restaurantId, restaurantName, eventId, eventTitle, eventStart, eventEnd, photoURLList])
                elif dtEventStart <= apr1 and dtEventEnd >= apr30:
                    events.append([restaurantId, restaurantName, eventId, eventTitle, eventStart, eventEnd, photoURLList])
                else:
                    continue

    eventsDf = pd.DataFrame(events, columns=["event_id", "res_id", "res_name", "photos", "event_title", "start_date", "end_date"])
    eventsDf.replace("", "NA", inplace=True)
    eventsDf.to_csv("task2.csv", index=False)

if __name__ == "__main__":
    main()