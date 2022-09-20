# IMPORT OS & CSV
import os
import csv

# DEFINE VARIABLES
candidate = ""
can_votes = {}
total_votes = 0
perc_of_candidate= {}
winner_total = 0
winner = ""

# CSV INTO OBJECT
with open("Resources/election_data.csv") as election_data:
    reader = csv.reader(election_data)

    # READ HEADER
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        
        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate in can_votes:
            can_votes[candidate] = can_votes[candidate] + 1
            
        else:
            can_votes[candidate] = 1   

# WINNER
for name, votes_ct in can_votes.items():
    perc_of_candidate[name] = "{0:.0%}".format(votes_ct/total_votes)
    if votes_ct > winner_total:
        winner_total = votes_ct
        winner = name

# PRINT TO TERMINAL
print("Election Results")
print("-----------------")
print(f" Total Votes: {total_votes}") 
print("-----------------")
for name, votes_ct in can_votes.items():
    print(f"{name}: {perc_of_candidate[name]} ({votes_ct})")
print("-----------------")
print(f"And the winner is: {winner}!")
print("-----------------")  

# EXPORT TO .TXT
with open("Analysis/output.txt", 'w') as f:
    print("Election Results", file=f)
    print("-----------------", file=f)
    print(f" Total Votes: {total_votes}", file=f) 
    print("-----------------", file=f)
    for name, votes_ct in can_votes.items():
        print(f"{name}: {perc_of_candidate[name]} ({votes_ct})", file=f)
    print("-----------------", file=f)
    print(f"And the winner is: {winner}!", file=f)
    print("-----------------", file=f)  