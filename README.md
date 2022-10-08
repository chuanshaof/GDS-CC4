# GDS-CC4
GovTech Internship 2023, GDS-CC4 submission, FOO CHUAN SHAO

# Setup and running of tasks

## Initial set up instructions
Move to the parent directory and install all Python dependencies with `pip3 install -r requirements.txt`.

## Running tasks
From the parent directory, move to the tasks directory with `cd tasks`. \
Run tasks using the command of `python task#.py`, filling up "#" with the desired task (1-3) \
(e.g. `python task1.py` will run task 1)

Alternatively, you can run this with any code editors using the "Run" button, or its equivalent.

## Running of tests
Similar to running tasks, however, move to the tests directory with `cd tests` followed by `python -m unittest` for all tests.\
Alternatively for individual tests, `python -m unittest tests.test#`, replacing "#" with the desired task (1-3)

# Assumptions, comments on data, and overview of code
## Assumptions made
1. (Task 1) Invalid Country-Code is regarded as missing data and is populated as NA
2. Missing data keys are replaced with "NA" instead of discarding the entire row
3. Leading and trailing whitespaces is to be removed
4. JSON data will always have the same structure and will have the same keys for a particular value
5. (Task 2) The duration of the event in April 2019 does not matter, as long as it has occurred for at least a second in April 2019.
6. (Task 3) Only exact matches in `rating_text` shall be considered.

## Comments on data
1. Some of the data may have special characters that can not be read by Python by default. To fix, encoding to 'utf-8' is required.
2. (Task 1) Strange data for all `country_id` of 17, where the city is dummy and the ratings are 0. To remove the data, uncomment line 28.
3. (Task 2) There may be more than 1 event photos, so they are populated in a list of photos.
4. (Task 3) Some of the `rating_text` are in another language other than English. However, translating these data may result in it becoming valid. To include these data, uncomment lines 26 to 40.

## Code
### Task 1
Task 1 simply reads through a JSON file and navigating through it using the appropriate list traversal and dictionary keys. The below demonstrates the methods and reasoning behind the design of the code.
1. Pandas is used for easy `.csv` and `.xlsx` management.
2. `.get` method is used for missing data keys as per stated in assumption 

### Task 2
Task 2 is similar to task 1 in getting the necessary information. However, it includes a condition to ensure that event is in April 2019.\
As per the condition, there are 3 particular cases where the event will happen on April 2019.\
1. If the start date is in April 2019
2. If the end date is in April 2019
3. If the event starts BEFORE April 2019 AND ends AFTER April 2019

### Task 3
Task 3 can have multiple approaches to calculating the threshold for the various ratings. The approach taken in the code is to simply pair the `rating_text` and the average corresponding `rating_score`. Other approaches may include machine learning.\
</br>
Additionally, there seems to be different languages for `rating_text`, which makes it difficult to translate. However, these texts when translated might give the expected keys for the various ratings. By assumption 6, these ratings are not considered even if the translation gives the expected results. \
However, as per comment 4, the consideration has also been coded in and will need to be uncommented to include these ratings. \
</br>
The output of this task will be printed on the terminal, otherwise the `main()` function will return the dictionary of the data.\
For the output printed on the terminal, the score will be rounded to 1 decimal place. 

## Testing
### Test 1
Test 1 tests for the flexibility of the code while dealing with JSON keys and missing values. This is the basic test to cover to ensure that the code works as expected. 

In this test, 2 files have been specifically modified to simulate the cases for missing keys and empty values. The expected outcome of the modified file is then used and asserted to match the actual outcome.

Test 1 can be further enhanced with more edge cases using fuzzy testing.

### Test 2
Test 2 handles the functionality and ensures the edge cases of the dates. There are a total of 6 cases that was tested and asserted if the event has occured in April 2019 or not.

In this test, missing keys and empty values has been omitted in the test due to time constraint. However, to do so, the same approach to test 1 can be taken to test comprehensively.

### Test 3
Test 3 ensures that the calculation for the average score has been done correctly and appropriately. For this test, the approach taken is to edit the file and expect for an outcome. 

The simplest and easiest test to create was to edit the rating for "Poor" since it has only one count. This also helped to test edge cases, and managed to fix 1 bug regarding the division of 0.