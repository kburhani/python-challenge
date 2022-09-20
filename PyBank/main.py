# IMPORT OS & CSV
import os
import csv

# CSV INTO OBJECT
budget_data = os.path.join("Resources", "budget_data.csv")

# DEFINE VARIABLES
total_months = 0 #(The total number of months included in the dataset)
total_pl = 0 #(The net total amount of "Profit/Losses" over the entire period)
value = 0 #(changes in "Profit/Losses" over the entire period, and then the average of those changes)
change = 0 #(changes in "Profit/Losses" over the entire period, and then the average of those changes)
dates = [] #(The greatest increase&decrease in profits (date and amount) over the entire period)
profits = [] #(The greatest increase&decrease in profits (date and amount) over the entire period)

# Open & read CSV file
with open('Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # READ HEADER
    csv_header = next(csvreader)

    # Read first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    # Going through each row of data after the header & first row 
    for row in csvreader:
        # tracking dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Total number of months
        total_months += 1

        # Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    # Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

# PRINT TO TERMINAL
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# EXPORT TO .TXT
with open("analysis/output.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("---------------------", file=f)
    print(f"Total Months: {str(total_months)}", file=f)
    print(f"Total: ${str(total_pl)}", file=f)
    print(f"Average Change: ${str(round(avg_change,2))}", file=f)
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})", file=f)
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})", file=f)