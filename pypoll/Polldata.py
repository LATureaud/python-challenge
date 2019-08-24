#import csv document
import os
import csv
#import file data
polldata = os.path.join('PyPoll.csv')



Candidates = []
votespercandidate = {}
Total = 0
percents = 0

with open(polldata) as Data:
    reader = csv.reader(Data)
    header = next(reader)
    
#create for loop to find the names of candidates
#while finding names find total of votes
#add +1 vote everytime for voter
    for row in reader: 
        Total += 1
        Name = row[2]
        if Name not in Candidates: 
            Candidates.append(Name)
            votespercandidate[Name]= 0
        votespercandidate[Name] = votespercandidate[Name] + 1
        #Calculate percentages of votes
    percents = []
    votelist = list(votespercandidate.values())
    for x in votelist:
        percents.append(round(int(x*100)/Total))

   #find max percentage(winner)
    winner = max(votespercandidate, key=votespercandidate.get)
        
    
        
    election = 0
    for x in range(len(Candidates)):
        print(str(Candidates[int(election)]) + ": " + str(percents[int(election)]) + "% (" + str(votelist[int(election)])+ ")")
        election += 1


print('ELECTION RESULTS')
print('________________________________')
print(votespercandidate)
print(Total)
print(percents)
print(winner)


        

#while looping for candidates calculate numbers of votes

#write formula to change total votes into a percentage

#write out the winner of the election
answer = ""
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.