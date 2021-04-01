import os
import csv

input_csvpath = os.path.join("Resources", "election_data.csv")
output_csvpath = os.path.join("analysis", "election_analysis.txt")

# set up empty list to hold candidate list

candidate_list = []

# set up counter for each candidate
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#set up empty winner variable
election_winner = ""

# set up votes counter

total_votes = 0

with open(input_csvpath) as file_handler:
    csvreader = csv.reader(file_handler, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        # set up variable to hold candidate's name
        candidate_name = row[2]
        # add candidates to list of candidates if they're not there already
        if candidate_name not in candidate_list :
            candidate_list.append(candidate_name)

        # add the votes to their corresponding counter
        if candidate_name == "Khan" :
            khan_votes += 1
        elif candidate_name == "Correy":
            correy_votes += 1
        elif candidate_name == "Li":
            li_votes += 1
        elif candidate_name == "O'Tooley":
            otooley_votes += 1
    
#Check to see who is the winner

if (khan_votes > correy_votes) and (khan_votes > li_votes) and (khan_votes > otooley_votes):
    election_winner = "Khan"
elif (correy_votes > li_votes) and (correy_votes > otooley_votes):
    election_winner = "Correy"
elif (li_votes > otooley_votes):
    election_winner = "Li"
else:
    election_winner = "O'Tooley"


#Calculate percentages

khan_percentage = round(((khan_votes/total_votes)*100), 2)
correy_percentage = round(((correy_votes/total_votes)*100), 2)
li_percentage = round(((li_votes/total_votes)*100), 2)
otooley_percentage = round(((otooley_votes/total_votes)*100), 2)

Output = (
    f'Election Results\n'
    f'--------------------\n'
    f'Total Votes: {total_votes}\n'
    f'--------------------\n'
    f'{candidate_list[0]}: {khan_percentage}% ({khan_votes})\n'
    f'{candidate_list[1]}: {correy_percentage}% ({correy_votes})\n'
    f'{candidate_list[2]}: {li_percentage}% ({li_votes})\n'
    f'{candidate_list[3]}: {otooley_percentage}% ({otooley_votes})\n'
    f'--------------------\n'
    f'Winner: {election_winner}\n'
)
print(Output)

with open(output_csvpath, "w") as output_file_handler:
    output_file_handler.write(Output)

