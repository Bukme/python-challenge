import pandas as pd
from pathlib import Path

#Create text output
f = open("election_analysis.txt", "w")

#create path to the csv file and read the csv file
election_path = Path("python-challenge/PyPoll/election_data.csv")
election_data = pd.read_csv(election_path)


#Print the election data head. If you'd like to see what it looks like. Delete the comment(hashtag) run the print statement
#print (election_data.head())

#Output the total number of votes cast
Total_votes = election_data["Ballot ID"].count()

print ("Total number of votes cast: ",Total_votes,file=f)
print(file=f)
print ("Total number of votes cast: ",Total_votes)
print()

    #Generate a complete list of candidates who received votes
list_of_candidate = election_data["Candidate"].unique()
print("List of candidates who received votes: ", list_of_candidate,file=f)
print(file=f)
print("List of candidates who received votes: ", list_of_candidate)
print()

#The percentage of votes each candidate won

#Group the votes by candidates first 
group_candidate = election_data.groupby("Candidate").count()

#drop the county column.We don't need it
grouped_candidate = group_candidate.drop(columns=['County'])

# Calculate the percentage from the grouped result
grouped_candidate['percentage'] = (grouped_candidate['Ballot ID'] / grouped_candidate['Ballot ID'].sum()) * 100
print("The percentage of vote each candidate won: \n",grouped_candidate.round(3),file=f)
print(file=f)
print("The percentage of vote each candidate won: \n",grouped_candidate.round(3))
print()

#Output winner
drop_ballot_id = grouped_candidate.drop(columns= ['Ballot ID'])
winner = drop_ballot_id.idxmax()
print("This is the candidate that has the highest vote by", winner,file=f)
print("This is the candidate that has the highest vote by", winner)


f.close()