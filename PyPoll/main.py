# Import Dependencies
import os
import csv

# Declare file location through pathlib
input_file = os.path.join("CSV-Resources", "election_data.csv")

# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(input_file,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Counting the total numbers of votes.
        total_votes +=1

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Zip lists together based candidate(key) and the total votes(value)
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the votes
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


# Set variable for output file
output_file = os.path.join("text-file-analysis","Election_Results.txt")

#  Open the output file
with open(output_file,"w") as file:

# Write in zipped rows
# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------\n")



