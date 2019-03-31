import os
import csv

highest = 0
highest_change = 0
highest_month = 0
lowest = 0
lowest_change = 0
lowest_month = 0
profit = 0

net_list = []
change = 0
change_list = []

# Navigate to the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")    
    # Skips header
    csv_header = next(csvfile, None)
    print(f"CSV Header: {csv_header}")
    
    # loops through ROW
    counter = 0
    for row in csvreader:
        
        counter = counter + 1
        
        profit += int(row[1])
        
        if int(row[1]) > highest:
            highest = int(row[1])
            highest_month = row[0]
        elif int(row[1]) < lowest:
            lowest = int(row[1])
            lowest_month = row[0]

        net = int(row[1]) # Remember that items in a list are strings by default.
        net_list.append(net)
        
n = 0
for n in range(85):
#     cur = net_list[n]
#     nxt = net_list[n + 1]
    change = net_list[n + 1] - net_list[n]
    change_list.append(change) # put changes into a list

avg_change = (sum(change_list)/len(change_list))

# Summary table
print("Financial Analysis")
print("----------")
print(f"Total Months: {counter}")
print(f"Total: ${profit}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profit: {highest_month} ${max(change_list)}")
print(f"Greatest Decrease in Profit: {lowest_month} ${min(change_list)}")