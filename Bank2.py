import os
import csv
#import csv file data
budget_data = os.path.join('Homework3A.csv')
#open the file and read it - skip the header line
with open(budget_data, mode = 'r') as csvfile:
   budget = csv.reader(csvfile, delimiter=',')
   next(budget)
#set up some variables
   maxrev = 0
   months = 0
   list1 = []
   monthlist = []
   change = []
#make a function may need to go back to it
   def changefunction(item):
       length = len(item)
       for x in range(length):
           change.append(int(item[x])-int(item[x-1]))
       change.pop(0)
       change.insert(0, 0)
       return None
#for loop add up the numbers and put them in list
   for row in budget:
       list1.append(row[1])
       maxrev += int(row[1])
       monthlist.append(row[0])
       months += 1

   changefunction(list1)
#zip lists to make a dictionary
   keys = (change)
   values = (monthlist)
   addtogether = dict(zip(keys, values))
#get the display going
   print("FINANCIAL ANALYSIS")
   print("-------------------------------")
   print("Total Months: " + str(months))
   print("Total: $" + str(maxrev)+".00")
   print("Average Change: $" + str(round(int(sum(change))/int(len(change))))+".00")
   increase = str(max(change))
   decrease = str(min(change))
   print("Greatest Increase in Profits: " + addtogether[int(increase)] + " $" + increase +".00")
   print("Greatest Decrease in Profits: " + addtogether[int(decrease)] + " $" + decrease +".00")
   open('Homework3A.csv')
print("done")
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period