import os
import csv

# create a path to your file
bank_csv = os.path.join("Resources", "budget_data.csv")

# 1) The total number of months 
# open and read csv
with open(bank_csv, 'r') as bank_csv_file:
    bank_csv_reader = csv.reader(bank_csv_file, delimiter=",")
    header = next(bank_csv_reader, None)  # skip the header row
    date_values = [row[0] for row in bank_csv_reader] # Extract values from date column
        
# Find the total months using len() and display using print()
total_months = len(date_values) 

# 2) The net total amount of "Profit/Losses" over the entire period
with open(bank_csv, 'r') as bank_csv_file:
    bank_csv_reader = csv.reader(bank_csv_file, delimiter=",")
    header = next(bank_csv_reader, None)
    profit_loss_values = [int(row[1]) for row in bank_csv_reader] # Extract values from profit/losses
    total_amount = sum(profit_loss_values) 

# 3) The changes in "Profit/Losses" over the entire period, and then the average of those changes
# Find the changes over a period for the range in the list date_values and assign to the variable changes 
changes = [profit_loss_values[i] - profit_loss_values[i - 1] for i in range(1, len(profit_loss_values))]
average_change = round(sum(changes) / len(changes), 2) 

# 4) The greatest increase in profits (date and amount) over the entire period
max_increase_index = changes.index(max(changes)) # find the max of changes and the index of the value

# find the date using the index of the max value
# Adding 1 because changes start from index 1
max_increase_date = date_values[max_increase_index + 1]  
max_increase = max(changes) 

# 5) The greatest decrease in profits (date and amount) over the entire period
min_increase_index = changes.index(min(changes))
min_increase_date = date_values[min_increase_index + 1]  
min_increase = min(changes)

# Specify the file path within the existing folder
output_file_path = os.path.join("analysis", "financial_analysis.txt")

# create a variable to contain your results/output to be printed
output = (
    "Financial Analysis\n"
    "-------------------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    f"Greatest Decrease in Profits: {min_increase_date} (${min_increase})"
)
# Export results to a text file
with open(output_file_path, 'w') as analysis_file:
    analysis_file.write(output)

print(output)