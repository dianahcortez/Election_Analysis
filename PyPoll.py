# add our dependencies
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save theh file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt") 

#Iniatalize a total vote counter.
total_votes = 0

#candidate_options and candidate votes
candidate_options = []
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the elections results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#read the header row.
    headers = next(file_reader)

#print each row in the CSV file:   
    for row in file_reader:
    #add to the total vote count
        total_votes += 1
        
    #print the candidate name from each row.
        candidate_name = row[2]

    #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
    
    #add it to the list of candidates
            candidate_options.append(candidate_name)

        #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    #save the results to our text file
with open(file_to_save, "w") as txt_file:    

#print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes : {total_votes:,}\n"
        f"-----------------------\n")

    print(election_results, end="")

    #save the final vote count to the text file
    txt_file.write(election_results)
    #determine the percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:
                #retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]   
                #calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
                #print the candidate name and percentage of votes.

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #save the candidate results to our text file
        txt_file.write(candidate_results)

    #determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent =
        #vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #print the winning candidates results to the terminal
    winning_candidate_summary = (    
        f"---------------------------\n"  
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")

print(winning_candidate_summary)

#save the winning candidates results to the text file.
txt_file.write(winning_candidate_summary)    


 


