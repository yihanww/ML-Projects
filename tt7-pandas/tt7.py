import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.
morgdf = pd.read_csv("data/morg_d07_strings.csv")

# TASKS 2-6
# For each of the tasks, print the value requested in the task.

# Task 2: Extract the "age" column from morg_df.
age = morgdf["age"]
age

# Task 3: Extract the row that corresponds to h_id 1_2_2 from morg_df.
hid = morgdf.loc["1_2_2"]
hid

# Task 4: Use slicing to extract the first four rows of morg_df.
firstfour = morgdf.loc[:4]
firstfour

# Task 5: Write a loop that identifies the columns that have at least one missing value and constructs a dictionary that maps these column names to zero. 
# Recall that you can access the column names for a dataframe via the columns attribute.
columns = {}
for column in morgdf.columns:
    if morgdf[column].isna().any():
        columns[column] = 0.0
columns

#Task 6: Use the fillna method to replace the missing values in the columns you identified in the previous task with zero. 
#Hint: take a careful look at the documentation and you’ll notice that the dictionary you constructed in the previous task will be useful for this task.
morgdf.fillna(value=columns, inplace=True)

# Task 7
# Convert the four string columns (ethnicity, gender, race, and employment status) to categoricals.
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

for category in TO_CATEGORICALS:
    if category in morgdf.columns:
        morgdf[category] = morgdf[category].astype("category")

# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8
boundaries = range(0, 99, 10)
morgdf.loc[:, "hwpw_bin"] = pd.cut(morgdf["hours_worked_per_week"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

print("Morg columns types after Task 8")
print(morgdf.dtypes)


### Tasks 9-13
# Task 9: Use filtering to extract all rows that correspond to a person who works 35 or more hours per week.
hwpw35 = (morgdf["hours_worked_per_week"] >= 35)
time_filter = morgdf[hwpw35]
time_filter

# Task 10: Use filtering to extract the rows that correspond to the people who are not working.
notworking = (morgdf["employment_status"])
notworking_filter = (morgdf["employment_status"] == "Working")
notworking_filter

# Task 11: Use filtering to extract the rows that correspond to people who worked at least 35 hours per week or who earned more than $1000 per week. 
#Hint: it might be useful to review the documentation on boolean indexing.
one_thousand = ((morgdf["hours_worked_per_week"] >= 35) |
               (morgdf["earnings_per_week"] > 1000))
one_thousand_filter = morgdf[one_thousand]

# Task 12: Use the value count method to count the number of people recorded for different races/race combinations and then print the five most frequent races (or combinations thereof).
race_counts = morgdf["race"].value_counts()[:5]
race_counts

# Task 13: Use the group by approach to count the number of people in each race/race combination.
race_group = morgdf.groupby("race").size().sort_index()

# Task 14
# Task 14 Use pd.merge and other pandas methods to produce a dataframe that contains a count of grades by major:
students = pd.read_csv("data/students.csv")
extended_grades = pd.read_csv("data/extended_grades.csv")
mergedf = pd.merge(students, extended_grades, on="UCID", how="inner")
mergedf
merge_group = mergedf.groupby(["Grade","Major"]).size().reset_index()
merge_group_rename = mergedf.rename(columns={0:"Count"}, inplace=True)
merge_group_rename