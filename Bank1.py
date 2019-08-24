import os
import csv

# Path to collect bank data

bank_csv = os.path.join('..', 'LearnPython', 'Homework3A.csv' )

def mean (numbers): 
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

def data(date):
    range(i, j)
    
    #Define the function and have it 
    month = str(date[0])
    total = int(sum(date[1]))
    avg = int(mean(date[1]))



# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on rows
    csvreader = csv.process(csvfile, delimiter=',')

       # Loop through the data
    for row in csvreader:

print(month)
print(total)
print(avg)