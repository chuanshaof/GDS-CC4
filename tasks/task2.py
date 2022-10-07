import pandas as pd
import datetime, utils

def main():
    # datetime object to format and compare dates
    # https://www.geeksforgeeks.org/converting-string-yyyy-mm-dd-into-datetime-in-python/
    dateTimeFormat = "%Y-%m-%d"

    # Reading data from URL
    rawData = utils.getJsonURL(utils.url)

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
                eventTitle = event.get("title", "").strip()
                eventStart = event.get("start_date", "").strip()
                eventEnd = event.get("end_date", "").strip()
                photoURLList = []

                for photo in event.get("photos", []):
                    photoURLList.append(photo.get("photo", {}).get("url", "").strip())

                if len(photoURLList) == 0:
                    photoURLList = ""

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
    eventsDf.to_csv("outputs/task2.csv", index=False)

if __name__ == "__main__":
    main()