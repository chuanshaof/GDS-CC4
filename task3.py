from urllib.request import urlopen
import pandas as pd
import json, sys, csv
from googletrans import Translator, constants

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
    
    # Read JSON file from url
    # https://www.geeksforgeeks.org/how-to-read-a-json-response-from-a-link-in-python/
    with urlopen(url) as response:
        rawData = json.loads(response.read().decode("utf-8"))
    
    # Content of ratings should be {"rating_text": [rating_sum, rating_count]}
    ratings = {"Excellent": [0, 0], "Very Good": [0, 0], "Good": [0, 0], "Average": [0, 0], "Poor": [0, 0], "Not rated": [0, 0]}


    # Loading the data as rows
    for data in rawData:
        for restaurant in data["restaurants"]:
            restaurant = restaurant["restaurant"]
            
            # Meant to handle missing dictionary keys
            # https://docs.python.org/3/library/stdtypes.html#dict.get
            userRatingText = restaurant.get("user_rating", {}).get("rating_text", "")
            userRating = restaurant.get("user_rating", {}).get("aggregate_rating", "")
            
            if userRatingText in ratings:
                ratings[userRatingText][0] = ratings[userRatingText][0] + float(userRating)
                ratings[userRatingText][1] = ratings[userRatingText][1] + 1
            else:
                # https://www.thepythoncode.com/article/translate-text-in-python
                translator = Translator()
                userRatingText = translator.translate(userRatingText, dest="en").text

                # https://www.programiz.com/python-programming/methods/string/casefold
                for key in ratings.keys():
                    if userRatingText.casefold() == key.casefold():
                        ratings[key][0] = ratings[key][0] + float(userRating)
                        ratings[key][1] = ratings[key][1] + 1
                        break
    
    for key in ratings.keys():
        ratings[key] = ratings[key][0] / ratings[key][1]
        
    print(ratings)

if __name__ == "__main__":
    main()
    