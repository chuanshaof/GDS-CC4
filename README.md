"# GDS-CC4" 

# Task 1
restaurant_data_bugged is missing keys in the dictionary, such as "city"

Assumptions:
    1. 

Comments on data:
    1. There are some issues with a country_id of 17, where the city is dummy and the ratings are 0. Strange data that might want to be removed.

Testing:
    1. restaurant_data_edited is a downloaded JSON file with a mising key in the dictionary for "city". This is to ensure that files will be able to be read even if some data is missing. These data are then later filled with NA if they are missing.
    2. 

# Task 2
Task 2 checks for the datetime of the system. In particular, for the month of April 2019. Assumption is to gather all events that have at least ONE hour of event in the month of April 2019.

ACCEPTED EVENTS:
    1. If start/end dates are in the month of April
    2. If event starts before the 1st of April AND ends after the 1st of April

Assumptions:
    1. All inputted items from the JSON file is copied exactly and nothing is changed.
    2. There are multiple pictures from a single event that is presented as a list.
    3. Even if the event was a second in the month of April 2019, it will be in the list.
    