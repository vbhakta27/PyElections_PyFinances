# Lists to store data
dict_finance={}
profit_losses = []
date =[]
avg_profit_losses = []
changes = []

# Allows us to creat file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Make sure that CSV file is a folder called Resources which is the in the same folder as main.py
csvpath = os.path.join('budget_data.csv')

# Open CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter as a comma and variable to hold contents
    budget_data = csv.reader(csvfile, delimiter=',')
    
    # Skips the header row first
    next(budget_data)
    
    # Loop through CSV to create lists of data
    for row in budget_data:
        profit_losses.append(row[0])
        date.append(row[1])
    
    # Fill dictionary of each month with its profit or loss
        if row[1] not in dict_finance.keys():
            dict_finance[row[1]] = row[0]

# Converts all string values of profits/losses into integers so they can be calculated on
profit_losses = [int(i) for i in profit_losses] 

# Loops through and gets the differences between each l
for i in range(len(profit_losses)-1):
    changes.append(profit_losses[i+1] - profit_losses[i])

# Calculates average of changes between each month
x = sum(changes)
denominator = len(changes)
avg_profit_losses = round(x/denominator,2)

# Gets total months by counting length of list dates
total_months = (len(date))

# Sums up all of list of profits/losses to get the total
total_profit_losses = sum(profit_losses)

# Stores maxs and mins on profit changes and their dates
max_change = (max(changes))
max_date = (date[changes.index(max(changes))+1])
min_change = (min(changes))
min_date = (date[changes.index(min(changes))+1])

# Prints tables
print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(total_months))
print('Total: $'+str(total_profit_losses))
print('Average Change: $'+str(avg_profit_losses))
print('Greatest Increase in Profits: '+max_date+' ($'+str(max_change)+')')
print('Greatest Decrease in Profits: '+min_date+' ($'+str(min_change)+')')

# Creates text file with results
f= open("PyFinances.txt","w+")
f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write('Total Months: '+str(total_months))
f.write('\nTotal: $'+str(total_profit_losses))
f.write('\nAverage Change: $'+str(avg_profit_losses))
f.write('\nGreatest Increase in Profits: '+max_date+' ($'+str(max_change)+')')
f.write('\nGreatest Decrease in Profits: '+min_date+' ($'+str(min_change)+')')
f.close() 