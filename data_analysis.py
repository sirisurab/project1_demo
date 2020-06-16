import os
import csv

cereal_csv_path = os.path.join("..", "Resources", "cereal_bonus.csv")

with open(cereal_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file

    # Read through each row of data after the header
    for row in csv_reader:

        # Convert row to float and compare to grams of fiber

        # enhancment data_story change cell number from 7 to 5
        if float(row[5]) >= 5:
            print(row)

