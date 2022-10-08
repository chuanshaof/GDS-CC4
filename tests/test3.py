from tasks import task3, utils
import unittest

# In both cases, the lone "Poor" rating has been manipulated
# Further testing can be done by creating JSON files, but will take time
class Task3Test(unittest.TestCase): 
    # Aggregae rating for "Poor" changed from 2.2 to 0
    def test_missing_rating(self):
        rawData = utils.getJsonLocal("inputs/restaurant_missing_ratings.json")
        output = task3.main(rawData)
        expectedOutput = {'Excellent': 4.666206896551727, 'Very Good': 4.21589085072231, 'Good': 3.7762237762237714, 'Average': 3.193333333333334, 'Poor': 0}

        assert (output == expectedOutput)

    # Rating text for "Poor" has been changed to ""
    def test_missing_rating_text(self):
        rawData = utils.getJsonLocal("inputs/restaurant_missing_ratings_text.json")
        output = task3.main(rawData)
        expectedOutput = {'Excellent': 4.666206896551727, 'Very Good': 4.21589085072231, 'Good': 3.7762237762237714, 'Average': 3.193333333333334, 'Poor': 0}

        assert (output == expectedOutput)

if __name__ == '__main__':
    unittest.main()