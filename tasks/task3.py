import utils
from googletrans import Translator

def main() -> dict:
    # Content of ratings will initially be {"rating_text": [rating_sum, rating_count]}
    ratings = {"Excellent": [0, 0], "Very Good": [0, 0], "Good": [0, 0], "Average": [0, 0], "Poor": [0, 0]}

    # Reading data from URL
    rawData = utils.getJsonURL(utils.url)

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
        ratings[key] = ratings[key][0] / ratings[key][1]

    return ratings

if __name__ == "__main__":
    ratings = main()

    with open("outputs/task3.txt", "w") as f:
        for key, value in ratings.items():
            print("{}: {:0.1f}".format(key, value))
            f.write("{}: {:0.1f}".format(key, value) + "\n")
    