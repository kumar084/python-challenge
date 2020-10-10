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
    #current_profit_loss = 0
    #change = []

    for row in csvreader:
        #print(row) 
        counter = counter + 1
       #adding the profit/loss rows to the list
        profit_loss.append(int(row[1]))

#         if counter = 0 then    
#             previous_profit_loss = 0    
#         else counter != 0   
#              change=int(row[1])-previous_profit_loss
#         change = change + 1 
#     print(change)

    print("Total months: " + str(counter) + ".")

    #summation of the list
    total = sum(profit_loss)
    print("Total: " + str(total) )

    # for i in range(len(profit_loss)-1):
    #     change_in_profit_loss = change.append(profit_loss[0+1]-profit_loss[0])
    #     print(change_in_profit_loss)
    #average = change_in_profit_loss/counter
    #print(average)
    
    #Copy Data into a txt file
    results=open("Analysis/results.txt","w")
    results.write("Financial Analysis \n------------------\n")
    results.write(f"Total Months: {counter}\n")
    results.write(f"Total: ${total}\n")