import os
import csv
# Path to collect data from the Resources folder
election_data = os.path.join( 'Resources', 'election_data.csv')
# Read in the CSV file
with open(election_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    #Skipping the header
    csv_header =next(csvreader)
    #Initializing variables
    counter = 0 
    #Initialize candidates list
    candidates = []
    comparison_list = []
   
    for row in csvreader:
        #print(row) 
        counter = counter + 1
       
        if row[2] in candidates:
            comparison_list[candidates.index(row[2])]+=1
        else:
            candidates.append(row[2])
            comparison_list.append(1)

    print("Total votes: " + str(counter) + ".")
    print(comparison_list)
    print(f"List of candidates: {candidates}")
    print(f"Votes won by each candidate: {comparison_list}")

     #Export Data into a text file
    results=open("Analysis/results.txt","w")
    results.write("Eelction Results \n------------------\n")
    results.write(f"Total Votes: {counter}\n")
    results.write(f"List of candidates: {candidates}")
    results.write(f"Votes won by each candidate: {comparison_list}")
    