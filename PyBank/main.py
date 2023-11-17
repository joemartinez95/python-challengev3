import os
import csv

pybank_csv = os.path.join('..','PyBank/Resources','budget_data.csv')

months = []
profits = []
changes = []


with open(pybank_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    previous_month = 0

    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
        
        if len(months) > 1:
            profit_change = int(row[1]) - previous_month
            changes.append(profit_change)
        else: 
            profit_change = 0
            changes.append(profit_change)
            
        previous_month = int(row[1])
        
    
    total = sum(profits)
    total_changes = sum(changes)
    average_change = total_changes / (len(months)-1)
    
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${total}')
    print(f'Average Change: ${"%.2f" % average_change}')
    print(f'Greatest Increase in Profits: {months[changes.index(max(changes))]} (${max(changes)})')
    print(f'Greatest Decrease in Profits: {months[changes.index(min(changes))]} (${min(changes)})')
  
with open('PyBank.txt', 'w') as f:
    f.write(f'Financial Analysis\n')
    f.write(f'----------------------------\n')
    f.write(f'Total Months: {len(months)}\n')
    f.write(f'Total: ${total}\n')
    f.write(f'Average Change: ${"%.2f" % average_change}\n')
    f.write(f'Greatest Increase in Profits: {months[changes.index(max(changes))]} (${max(changes)})\n')
    f.write(f'Greatest Decrease in Profits: {months[changes.index(min(changes))]} (${min(changes)})')
  
   


