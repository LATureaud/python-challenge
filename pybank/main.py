import os
import csv
#import csv file data
budget_data = os.path.join('Homework3A.csv')
with open(budget_data) as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    next (budget)

    total = 0
    changelist = []
    firstlist = []
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmont = ""
    lastmonth = None
    changes = []
     
    for row in budget:
        months = len(list(budget))
        total += int(row[1])
        month = row[0]
        pnl = row [1]
        total += int(pnl)
        months += 1
        #keeps a running maximum
        if lastmonth is not False:
            changes.append(int(pnl-str(lastmonth)))
            currentchange = pnl - lastmonth        
            if pnl > maxrev:
                maxrev = pnl
                maxmonth = month
            elif pnl < minrev:
                minrev = pnl
                minmonth = month

        lastmont = pnl
    avgchange = sum(changes)/len(changes)

return [months, total, maxrev, minrev,avgchange]
        
       


print ('Budget')
print("done")


