import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join( 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Skipping the header
    csv_header =next(csvreader)
    
    #Initialize profit_loss list
    profit_loss = []
    #Initializing variables
    counter = 0 
    previous_profit_loss = 0
    current_profit_loss = 0

    for row in csvreader:
        #print(row) 
        counter = counter + 1
       #adding the profit/loss rows to the list
        profit_loss.append(int(row[1]))

    print("Total months: " + str(counter) + ".")

    #print(profit_loss)

    #summation of the list
    total = sum(profit_loss)
    print("Total: " + str(total) )

    
    
