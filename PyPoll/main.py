# create a Python script that analyzes the votes and calculates each of the following:
# -- The total number of votes cast
# -- A complete list of candidates who received votes
# -- The percentage of votes each candidate won
# -- The total number of votes each candidate won
# -- The winner of the election based on popular vote.

# Import dependencies 
import os
import csv
import collections
from collections import Counter

# Define variables
candidates = []
candidate_votes = []

# Path to collect data
election_data = os.path.join("Resources/election_data.csv")

# open and read
with open(election_data, newline="") as file:
    reader = csv.reader(file, delimiter=",")

    # read header 
    header = next(file)

    # read thorugh each row after header
    #print(f"header: {header}") = header: Voter ID,County,Candidate
    for row in election_data:
        candidates.append(row[2])

    # sort list by candidates
    list_sorted = sorted(candidates)
  
    # count votes per candidate
    candidate_count = Counter(list_sorted)
    candidate_votes.append(candidate_count.most_common())
print(f"candidate: {candidate_count}.unique")
    # calculate percentage of votes won per candidate
    for item in candidate_votes
        first = 
        second =
        third =
        fourth = 

    # calculate total number of votes won per candidate


    # Popular vote winner  


# print to terminal 


# export results to text file

