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
   
    for row in csvreader:
        #print(row) 
        counter = counter + 1
    print("Total votes: " + str(counter) + ".")

     #Export Data into a text file
    results=open("Analysis/results.txt","w")
    results.write("Eelction Results \n------------------\n")
    results.write(f"Total Votes: {counter}\n")