# create a Python script that analyzes the votes and calculates each of the following:
# -- The total number of votes cast
# -- A complete list of candidates who received votes
# -- The percentage of votes each candidate won
# -- The total number of votes each candidate won
# -- The winner of the election based on popular vote.

# Import dependencies 
import os
import csv


# Define variables
candidates = ""
votes = 0
list_storage = []

winner_votes = 0
winner_name = ""

# Path to collect data
election_data = os.path.join("Resources/election_data.csv")

# open and read, split on comma
with open(election_data, newline="") as file:
    reader = csv.reader(file, delimiter=",")

    # skip header 
    header = next(file)

    for row in election_data:

        # Add to vote total
        votes += 1

        #add candidate name or add to existing
        candidates = row[2]

        if candidates in list_storage:
            list_storage[candidates] += 1
        else:
            list_storage[candidates] = 1

# calculating percentage & candidate votes
percentage = (list_storage[candidates]/votes)*100

# determine winner
if list_storage[candidates] > winner_votes:
    winner_votes = list_storage[candidates]
    winner_name = candidates

# print results to terminal 
results = ("Election Results",
"----------------------",
f"Total Votes: {votes}",
"----------------------",
f"{candidates}: {percentage}% ({list_storage[candidates]}", 
"----------------------",
f"Winner: {winner_name}")

print(results)

# export results to text file
write_results = os.path.join("analysis.txt")
with open(write_results,'w+') as textfile:
    textfile.write(str(results))