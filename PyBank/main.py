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
    positive_shift = 0
    negative_shift = 0
    
    #change = []
    for row in csvreader:
        #print(row) 
        counter = counter + 1
       #adding the profit/loss rows to the list
        profit_loss.append(int(row[1]))
        if counter == 0:    
            previous_profit_loss = 0    
        else:
            change=int(row[1])-previous_profit_loss
            change = change + 1 
    #print(change)

        if change>positive_shift:
                positive_shift=change
        else:
                negative_shift=change

    print("Total months: " + str(counter) + ".")
    #summation of the list
    total = sum(profit_loss)
    print("Total: " + str(total) )
    
    #average change
    average = round(change/counter)
    print("Average Change = " + str(average))

    #Greatest Increase and Decrease
    print("Greatest Increase in Profits:" + str(positive_shift))
    print("Greatest Decrease in Profits:" + str(negative_shift))

    #Export Data into a text file
    results=open("Analysis/results.txt","w")
    results.write("Financial Analysis \n------------------\n")
    results.write(f"Total Months: {counter}\n")
    results.write(f"Total: ${total}\n")
    results.write(f"Average Change: ${average}\n")
    results.write(f"Greatest Increase in Profits: ${positive_shift}\n")
    results.write(f"Greatest Decrease in Profits:  ${negative_shift}")
