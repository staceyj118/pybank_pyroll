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
winner_dictionary = {}
winner_votes = 0
winner_name = ""

# Path to collect data
election_data = os.path.join("Resources/election_data.csv")

# open and read, split on comma
with open(election_data) as file:
    reader = csv.reader(file)

    # skip header 
    header = next(reader)

    for row in reader:

        # Add to vote total
        votes += 1

        #add candidate name or add to existing
        candidates = row[2]

        if candidates not in list_storage:
            list_storage.append(candidates)
            winner_dictionary[candidates] = 0
        winner_dictionary[candidates] += 1
# print(winner_dictionary)
# print(votes)

# determine winner
# if list_storage[candidates] > winner_votes:
#     winner_votes = list_storage[candidates]
#     winner_name = candidates

for candidate in winner_dictionary:
    vote = winner_dictionary.get(candidate)
    percentage = float(vote)/votes
    if vote > winner_votes: 
        winner_votes = vote
        winner_name = candidate
# print(winner_name)
# print(winner_votes)

#print results to terminal 
results = (f"Election Results\n"
f"----------------------\n"
f"Total Votes: {votes}\n"
f"----------------------\n"
f"{candidates}: {winner_dictionary[candidate,percentage]}\n"
f"----------------------\n"
f"Winner: {winner_name}\n")

print(results)

# export results to text file
write_results = os.path.join("analysis.txt")
with open(write_results,'w+') as textfile:
    textfile.write(str(results))