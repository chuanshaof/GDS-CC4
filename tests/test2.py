from tasks import task2
import unittest, datetime

# Tests involving missing keys/data has been omitted here
# Tests have been reduced to specifically for dates
class Task2Test(unittest.TestCase): 
    # Class variable
    dateTimeFormat = "%Y-%m-%d"    

    # Start Apr 01, end 2022
    def test_start_apr1(self):
        startDate = datetime.datetime.strptime("2019-04-01", self.dateTimeFormat)
        endDate = datetime.datetime.now()
        assert(task2.in_april_2019(startDate, endDate))

    # Start Apr 30, end 2022
    def test_start_apr30(self):
        startDate = datetime.datetime.strptime("2019-04-30", self.dateTimeFormat)
        endDate = datetime.datetime.now()
        assert(task2.in_april_2019(startDate, endDate))

    # Start May 01, end 2022
    def test_start_may1(self):
        startDate = datetime.datetime.strptime("2019-05-01", self.dateTimeFormat)
        endDate = datetime.datetime.now()
        assert(task2.in_april_2019(startDate, endDate) == False)

    # Start Mar 31, end Apr 01
    def test_end_apr1(self):
        startDate = datetime.datetime.strptime("2019-03-31", self.dateTimeFormat)
        endDate = datetime.datetime.strptime("2019-04-01", self.dateTimeFormat)
        assert(task2.in_april_2019(startDate, endDate))

    # Start Mar 01, end Mar 31
    def test_end_mar31(self):
        startDate = datetime.datetime.strptime("2019-03-01", self.dateTimeFormat)
        endDate = datetime.datetime.strptime("2019-03-31", self.dateTimeFormat)
        assert(task2.in_april_2019(startDate, endDate) == False)

    # Start Mar 01, end Apr 30
    def test_end_apr30(self):
        startDate = datetime.datetime.strptime("2019-03-01", self.dateTimeFormat)
        endDate = datetime.datetime.strptime("2019-04-30", self.dateTimeFormat)
        assert(task2.in_april_2019(startDate, endDate))

if __name__ == '__main__':
    unittest.main()