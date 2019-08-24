import os
import csv
#import csv file data
import pandas as pd

poll_data = pd.read_csv(poll_data_df)
poll_data_pd.head()
poll_data_pd['Candidate'].value_counts()


Candidate = poll_data_pd['Candidate'].value_counts()
Name = poll_data_pd['Candidate'].unique()
print(Name)
print(Candidate)

n_list = Name.tolist()
print(n_list[0])

p_list = Candidate.tolist()
print(p_list)

sum = Total_votes.sum()
print(sum)
Total_percent = (Total_votes/sum)*100
print(Total_percent)

t_list = Total_percent.tolist()
print(t_list)

#create dictionary and DataFrame to see results
dic = {"Candidate": n_list, "Total Votes": p_list, "Percentages": t_list   
    }
result_df = pd.DataFrame(dic)
print(result_df)

print("done")
