import os
import csv
#import csv file data
budget_data = os.path.join('Homework3A.csv')
with open(budget_data) as csvfile:
    budget = csv.reader(csvfile, delimiter=',')

    next (budget)
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmont = ""
    lastmonth = None
    changes = []
    for row in csv:
        month = row[0]
        pnl = row [1]
        total += pnl
        months += 1
        #keeps a running maximum
        if lastmonth is not False:
            changes.append(pnl-lastmonth)
            currentchange = pnl - lastmonth        
            if pnl > maxrev:
                maxrev = pnl
                maxmonth = month
            elif pnl < minrev:
                minrev = pnl
                minmonth = current_month
        
        lastmonth = pnl
    avgchange = sum(changes)/len(changes)

    return [months, total, maxrev, minrev,avgchange]

    with open(path) as file:
print(return)        
        

