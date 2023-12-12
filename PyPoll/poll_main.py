import os
import csv

# create a path to your 
# create a variable to store the index for candidates
POLL_CSV_PATH = os.path.join("Resources", "election_data.csv")
CANDIDATE_NAME_INDEX = 2

# open and read csv
with open(POLL_CSV_PATH, 'r') as poll_csv_file:
    poll_csv_reader = csv.reader(poll_csv_file, delimiter = ",")
    header = next(poll_csv_reader, None) # skip the header row
    total_votes = 0 # set total votes to zero
    candidate_votes = {} # initialize dictionary to store the count for each candidate
    unique_candidates = [] # initialize a list to store unique candidates
    
    # 1) The total number of votes cast 
    # 2) A complete list of candidates who received votes
    for row in poll_csv_reader:
        total_votes += 1
        candidate = row[CANDIDATE_NAME_INDEX]  
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            unique_candidates.append(candidate)
            candidate_votes[candidate] = 1

# 3) The percentage of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on popular vote
vote_percentages = ""
winning_votes = 0
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    vote_percentages += f"{candidate}: {percentage:.3f}% ({votes} votes)\n"
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate
        
# create a variable to contain your results/output to be printed      
output = (
    "Election Results\n"
    "-------------------------------------------------------------\n"
    f"Total Number of Votes: {total_votes}\n"
    "-------------------------------------------------------------\n"
    "Percentage of Votes and Total Votes for Each Candidate:\n"
)
output += vote_percentages
output += (
    "-------------------------------------------------------------\n"
    f"Winner: {winner}"
)

# Create path for your output
OUTPUT_FILE_PATH = os.path.join("analysis", "election_analysis.txt")

# Export results to a text file
with open(OUTPUT_FILE_PATH, 'w') as analysis_file:
    analysis_file.write(output)
# Results written to election_analysis.txt
print(output)