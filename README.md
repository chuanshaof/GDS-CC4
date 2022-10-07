# GDS-CC4
GovTech Internship 2023, GDS-CC4 submission

# Setup and running of tasks

## Initial set up instructions
Move to the parent directory and install all Python dependencies with `pip3 install -r requirements.txt`

## Running tasks
From the parent directory, move to the tasks directory with `cd tasks`.
Run tasks using the command of `python task#.py`, filling up "#" with the desired task (1-3)
e.g. `python task1.py` will run task 1

Alternatively, you can run this with any code editors using the "Run" button, or its equivalent.

## Running of tests
Similar to running tasks, however, move to the tests directory with `cd tests` followed by `python test#.py`

# Assumptions made and comments on data
## Task 1
### Assumptions:




# Task 1
Assumptions:
    1. 

Comments on data:
    1. There are some issues with a country_id of 17, where the city is dummy and the ratings are 0. Strange data that might want to be removed.

Testing:
    1. restaurant_data_edited is a downloaded JSON file with a mising key in the dictionary for "city". This is to ensure that files will be able to be read even if some data is missing. These data are then later filled with NA if they are missing.
    2. 

# Task 2
ACCEPTED EVENTS:
    1. If start/end dates are in the month of April
    2. If event starts before the 1st of April AND ends after the 1st of April

Assumptions:
    1. All inputted items from the JSON file is copied exactly and nothing is changed.
    2. There are multiple pictures from a single event that is presented as a list.
    3. Even if the event was a second in the month of April 2019, it will be in the list.
    
# Task 3
Task 3 is simple, but challenging. After a quick scan of the system, there appears to be different languages for rating_text, which makes it difficult to translate in a general form. 

A simple way to find the aggregate is simply to pair the rating text and average rating score.

Skvělé, Muito Bom, Velmi dobré, Eccellente, Bardzo dobrze, Skvělá volba, Bueno, Excelente, Muy Bueno, Terbaik

We do not need to consider other factors and just bring in any data that is filled.

Output will be as such:
    Rating: Score (Rounded to 1 decimal place)

If the translated text does not match the original expected text, then we will ignore the rating as translations can be sensitive and may actually mean other things.

Things to consider for this, if one data is missing, e.g. text or rating, then the data cannot be used as it should come as a pair.

3 possible solutions:
    1. Create a dictionary of translations if possible, but will not be entirely exhausive
    2. Use an external library/API to translate
    3. Any rating not in English will be classified as "Good", which is the middle rating, but not ideal as it is expected to cause skews