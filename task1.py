from urllib.request import urlopen
import pandas as pd
import json, sys, csv

def main():
    # https://stackoverflow.com/questions/71459981/how-to-solved-charmap-codec-cant-encode-character-u300b
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    # Reading csvfile using pandas and converting it into a dictionary
    # Format will be {country_code: country_name}
    countries = {}
    countryDf = pd.read_excel("Country-Code.xlsx")
    for i in countryDf.index:
        countries[countryDf["Country Code"][i]] = countryDf["Country"][i]

    # ----------------- Reading JSON file -----------------
    # Change url here to what is necessary
    url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
    
    # # https://pythonbasics.org/pandas-json/
    # # 1. Reading json file using pandas
    # df = pd.read_json(url)
    # rawData = df.to_dict()

    # # 2. Read JSON file from local file directory
    # with open("restaurant_data_bugged.json", "r", encoding='utf-8') as f:
    #     rawData = json.load(f)
    
    # 3. Read JSON file from url
    # https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
    with urlopen(url) as response:
        rawData = json.loads(response.read().decode("utf-8"))
        
    restaurants = []
    # Loading the data as rows
    for data in rawData:
        for restaurant in data["restaurants"]:
            restaurant = restaurant["restaurant"]
            
            # Meant to handle missing dictionary keys
            # https://docs.python.org/3/library/stdtypes.html#dict.get
            id = restaurant.get("R", {}).get("res_id", "")
            name = restaurant.get("name", "")
            country = countries.get(restaurant.get("location", {}).get("country_id", ""), "")
            city = restaurant.get("location", {}).get("city", "")
            userRatingVotes = restaurant.get("user_rating", {}).get("votes", "")
            userRating = restaurant.get("user_rating", {}).get("aggregate_rating", "")
            cuisines = restaurant.get("cuisines", "")

            restaurants.append([id, name, country, city, userRatingVotes, userRating, cuisines])

    restaurantsDf = pd.DataFrame(restaurants, columns=["res_id", "name", "country", "city", "votes", "rating", "cuisines"])
    restaurantsDf.replace("", "NA", inplace=True)
    restaurantsDf.to_csv("task1.csv", index=False)

    # # https://docs.python.org/3/library/csv.html
    # with open('task1.csv', 'w', encoding="utf-8") as file:
    #     writer = csv.writer(file, lineterminator='\n')

    #     # Write the header of the file
    #     writer.writerow(["res_id", "name", "country", "city", "aggregate_rating", "cuisines"])
    #     writer.writerows(restaurantRows) 


if __name__ == "__main__":
    main()
    