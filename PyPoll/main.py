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
candidates = []

candidate_votes = 0

# Path to collect data
election_data = os.path.join("Resources/election_data.csv")

# open and read
with open(election_data, newline="") as file:
    reader = csv.reader(file, delimiter=",")

    # read header 
    header = next(file)

    # read thorugh each row after header
    #print(f"header: {header}") = header: Voter ID,County,Candidate
    # for row in election_data:
    #     candidates.append(row[2])

    # sort by candidate name 
    organized_list = sorted(candidates)
    print(organized_list)



    # count votes per candidate

    # calculate percentage of votes won per candidate

    # calculate total number of votes won per candidate

    # Popular vote winner  


# print to terminal 
results = (["Financial Analysis",
"----------------------",
f"Total Months: {len(total_months)}",
f"Total: {sum(net)}",
f"Average Change: ${average}",
f"Greatest Increase in Profits: {best_month} (${greatest_increase})",
f"Greatest Decrease in Profits: {worst_month} (${lowest_increase})"])

print(results)

# export results to text file
write_results = os.path.join("analysis.txt")
with open(write_results,'w+') as textfile:
    textfile.write(str(results))