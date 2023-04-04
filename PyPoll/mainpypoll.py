# Modules
import os
import csv

# Define the path to the csv file
pypoll_csv = os.path.join("/Users/arminearutyunyan/Desktop/python-challenge1/python-challenge/PyPoll/Resources/election_data.csv")

# Dfining the variables
votes = 0

# Defining the lists and dictionaries
cand_list = []
cand_name = []
cand_votes = {}
win_votes = 0
win_perc = 0
percetage = 0
win_cand = 'None'




# Open the csv with the csv.reader
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Header
    csv_header = next(csvfile)

    # Opening a loop for each row
    for row in csv_reader:
    
        # Finding a total votes
        votes +=1 
    
        cand_name = row[2]

        # Creating a candidate list and adding candidates to the list
        if cand_name not in cand_list:
            cand_list.append(cand_name)
            cand_votes[cand_name] = 0

        cand_votes[cand_name] +=1
        
        
# Terminal printing
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {votes}") 
    print("------------------------------")

# text file printing. Defining the path to the output file and opening it with "w"
output_1_file = os.path.join("/Users/arminearutyunyan/Desktop/PythonStuff/output/output_1_file.txt")
with open(output_1_file, "w") as txt_file:  
    txt_file.write("Election Results\n")
    txt_file.write("------------------------------\n")
    txt_file.write(f"Total Votes: {votes}\n")
    txt_file.write("------------------------------\n")

    
    
# Finding the votecount for each candidate through the loop
    votecount = 0    
    for cand_name in cand_list:
        votecount = cand_votes.get(cand_name)
        percentage = float(votecount)/float(votes)*100


# Terminal printing
        print(f"{cand_name}: {percentage:.3f}% ({votecount:})\n")
  # Text file printing
        txt_file.write(f"{cand_name}: {percentage:.3f}% ({votecount:})\n") 
        
    
    
        # using if condition to find the winner candidate name
        
        if votecount > win_votes:

            win_votes = votecount
            win_cand = cand_name

        
        
           
        
   # Text file printing
    txt_file.write("------------------------------\n")
    txt_file.write(f"Winner: {win_cand}\n")             

    # Terminal printing
    print("------------------------------")    
    print(f"Winner: {win_cand}") 

















        




                        



        

    
        


    

    



