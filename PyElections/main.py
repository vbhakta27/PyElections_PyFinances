# Lists to store data
dictVoting = {}
SortedByVotes_dictVoting =[]
total_votes = 0
percent_votes = []

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
    
    # Skips the header row first
    next(csvreader)
    
    # Loop through CSV to get lists of data
    for row in csvreader:

        # Keeps a count of total vote entries
        total_votes +=1
        
        # Fill dictionary of unique candidate names. Everytime it comes across a unique candidate store it as a key and set its value to 1. 
        # If that candidates name comes up again then add 1 to its stored value to get a total vote count for that candidate.
        if row[0] not in dictVoting.keys():
            dictVoting[row[0]] = 1
        else:
            dictVoting[row[0]] += 1

# Create a sorted list by descending votes
import operator
SortedByVotes_dictVoting = sorted(dictVoting.items(), key=operator.itemgetter(1),reverse=True)

# Create a list of percent votes for each candidate
for candidate, votes in SortedByVotes_dictVoting:
    percent_votes.append(votes/total_votes)

# Print out results table
print('Houston Mayoral Election Results')
print('-----------------------------------------')
print('Total Cast Votes: ' + str(total_votes))
print('-----------------------------------------')

x = 0
for key,value in SortedByVotes_dictVoting:
    percent = percent_votes[x]
    print(f"{key}: {round(percent*100, 2)}% ({value})")
    x += 1

print('-----------------------------------------')
print('1st Advancing Candidate: ' + SortedByVotes_dictVoting[0][0])
print('2nd Advancing Candidate: ' + SortedByVotes_dictVoting[1][0])
print('-----------------------------------------')


f= open("PyElections.txt","w+")
f.write('Houston Mayoral Election Results\n')
f.write('-----------------------------------------\n')
f.write('Total Cast Votes: ' + str(total_votes))
f.write('\n-----------------------------------------\n')

x = 0
for key,value in SortedByVotes_dictVoting:
    percent = percent_votes[x]
    f.write(f"{key}: {round(percent*100, 2)}% ({value})\n")
    x += 1

f.write('-----------------------------------------\n')
f.write('1st Advancing Candidate: ' + SortedByVotes_dictVoting[0][0])
f.write('\n2nd Advancing Candidate: ' + SortedByVotes_dictVoting[1][0])
f.write('\n-----------------------------------------\n')
f.close() 