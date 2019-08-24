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
    for row in budget:
        month = row[0]
        profitloss = int(row[1])
        total += int(row[1])
        months += 1
        #keeps a running maximum
        if lastmonth is not False:
            changes.append(profitloss-lastmonth)
            currentchange = profitloss - lastmonth        
            if profitloss > maxrev:
                maxrev = profitloss
                maxmonth = month
            elif profitloss < minrev:
                minrev = profitloss
                minmonth = month
        
        lastmonth = profitloss
    avgchange = sum(changes)/len(changes)

print([months, total, maxrev, minrev,avgchange])