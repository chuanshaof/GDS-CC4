import pandas as pd
import datetime, utils

def main(rawData) -> None:
    # datetime object to format and compare dates
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

                if in_april_2019(dtEventStart, dtEventEnd):
                    events.append([eventId, restaurantId, restaurantName, photoURLList, eventTitle, eventStart, eventEnd])
                else:
                    continue

    eventsDf = pd.DataFrame(events, columns=["Event Id", "Restaurant Id", "Restaurant Name", "Photo URL", "Event Title", "Event Start Date", "Event End Date"])
    eventsDf.replace("", "NA", inplace=True)
    eventsDf.to_csv("outputs/restaurant_events.csv", index=False)

def in_april_2019(startDate: datetime, endDate: datetime) -> bool:
    apr1 = datetime.datetime(2019, 4, 1)
    apr30 = datetime.datetime(2019, 4, 30)

    if startDate >= apr1 and startDate <= apr30:
        return True
    elif endDate >= apr1 and endDate <= apr30:
        return True
    elif startDate <= apr1 and endDate >= apr30:
        return True
    else:
        return False

if __name__ == "__main__":
    # Reading data from URL
    rawData = utils.getJsonURL(utils.url)
    main(rawData)