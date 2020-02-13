# Lists to store data
candidate = []
county = []
voter_id = []
unique_candidates = []
vote_count = []
data_set=[]

# Allows us to creat file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Make sure that CSV file is in same folder as python code
csvpath = os.path.join('houston_election_data.csv')

# Open CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter as a comma and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Loop through CSV to get lists of data
    for row in csvreader:

        # Create array of data from CSV
        data_set.append(row)

        # Fill candidate variable
        candidate.append(row[0])

        # Fill county variable
        county.append(row[1])

        # Fill voter_id variable
        voter_id.append(row[2])

    
    # Loop through candidates to creat a list of unique candidates
    for x in candidate:
        if x not in unique_candidates:
            unique_candidates.append(x)
    print(unique_candidates)


    # Loop through candidates and get a count of how many times a unique candidate name appeared
    for name in unique_candidates:      
        vote_count.append(candidate.count(name))
    print(vote_count)
