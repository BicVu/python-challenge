import os
import csv

# Navigate to the file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data_csv, newline="") as csvfile:
    # Access csv library. Read this csvfile.
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skips header
    csv_header = next(csvfile, None)
    # prints header
    print(f"Header: {csv_header}")


# The total number of months included in the dataset.
# for loop must be nested in "with open" loop.
    for months in range(csvreader):
        # months =+ months
        print(months)

# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period