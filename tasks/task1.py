import pandas as pd
import utils

def main():
    # Reading csvfile using pandas and converting it into a dictionary
    # Format will be {country_code: country_name}
    countries = {}
    countryDf = pd.read_excel("inputs/Country-Code.xlsx")
    for i in countryDf.index:
        countries[countryDf["Country Code"][i]] = countryDf["Country"][i]

    # Reading data from URL
    rawData = utils.getJsonURL(utils.url)
    
    # List to keep track of restaurants
    restaurants = []
    # Loading the data as rows
    for data in rawData:
        for restaurant in data["restaurants"]:
            restaurant = restaurant["restaurant"]
            
            # Meant to handle missing dictionary keys
            # https://docs.python.org/3/library/stdtypes.html#dict.get
            id = restaurant.get("R", {}).get("res_id", "")
            name = restaurant.get("name", "").strip()
            country = countries.get(restaurant.get("location", {}).get("country_id", ""), "").strip()
            # Uncomment elow to remove empty/invalid country codes
            # if country == "": continue
            city = restaurant.get("location", {}).get("city", "").strip()
            userRatingVotes = restaurant.get("user_rating", {}).get("votes", "")
            userRating = float(restaurant.get("user_rating", {}).get("aggregate_rating", ""))
            cuisines = restaurant.get("cuisines", "").strip()

            restaurants.append([id, name, country, city, userRatingVotes, userRating, cuisines])

    restaurantsDf = pd.DataFrame(restaurants, columns=["Restaurant Id", "Restaurant Name", 
                                                        "Country", "City", "User Rating Votes", 
                                                        "User Aggregate Rating (in float)", "Cuisines"])

    # .replace is used to replace empty strings, it may be the case where the input was "" in the first place.
    restaurantsDf.replace("", "NA", inplace=True)
    restaurantsDf.to_csv("outputs/restaurants.csv", index=False) 

if __name__ == "__main__":
    main()
    