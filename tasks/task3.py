import utils
from googletrans import Translator

def main(rawData) -> dict:
    # Content of ratings will initially be {"rating_text": [rating_sum, rating_count]}
    ratings = {"Excellent": [0, 0], "Very Good": [0, 0], "Good": [0, 0], "Average": [0, 0], "Poor": [0, 0]}

    # Assume that the range is from 0 to 5
    ratingMin = {"Excellent": 5.1, "Very Good": 5.1, "Good": 5.1, "Average": 5.1, "Poor": 5.1}
    ratingMax = {"Excellent": -0.1, "Very Good": -0.1, "Good": -0.1, "Average": -0.1, "Poor": -0.1}

    # Loading the data as rows
    for data in rawData:
        for restaurant in data["restaurants"]:
            restaurant = restaurant["restaurant"]
            
            userRatingText = restaurant.get("user_rating", {}).get("rating_text", "")
            userRating = restaurant.get("user_rating", {}).get("aggregate_rating", "")

            if userRatingText == "" or userRating == "":
                continue

            if userRatingText in ratings:
                ratings[userRatingText][0] = ratings[userRatingText][0] + float(userRating)
                ratings[userRatingText][1] = ratings[userRatingText][1] + 1

                if ratingMin[userRatingText] > float(userRating):
                    ratingMin[userRatingText] = float(userRating)

                if ratingMax[userRatingText] < float(userRating):
                    ratingMax[userRatingText] = float(userRating)

            # # NOTE: Add this if language translation is desired
            # # Adding such that this does not get translated, runs faster
            # elif userRatingText == "Not rated":
            #     continue 
            # else:
            #     # https://www.thepythoncode.com/article/translate-text-in-python
            #     translator = Translator()
            #     userRatingText = translator.translate(userRatingText, dest="en").text

            #     # https://www.programiz.com/python-programming/methods/string/casefold
            #     for key in ratings.keys():
            #         if userRatingText.casefold() == key.casefold():
            #             ratings[key][0] = ratings[key][0] + float(userRating)
            #             ratings[key][1] = ratings[key][1] + 1
            #             break
    
    for key in ratings.keys():
        if ratings[key][1] == 0:
            ratings[key] = 0
        else:
            ratings[key] = ratings[key][0] / ratings[key][1]
        
    for key, value in ratingMax.items():
        print("Max: {}: {:0.1f}".format(key, value))

    for key, value in ratingMin.items():
        print("Min: {}: {:0.1f}".format(key, value))

    return ratings

if __name__ == "__main__":
    # Reading data from URL
    rawData = utils.getJsonURL(utils.url)
    ratings = main(rawData)

    with open("outputs/task3.txt", "w") as f:
        for key, value in ratings.items():
            print("{}: {:0.1f}".format(key, value))
            f.write("{}: {:0.1f}".format(key, value) + "\n")
    