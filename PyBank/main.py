import os
import csv

#loading up the path for the CSV to read
input_csvpath = os.path.join("Resources", "budget_data.csv")

#creating the path for the CSV file to wirte
output_csvpath = os.path.join("analysis","budget_analysis.txt")


#opening the csv from csvpath

with open(input_csvpath) as file_handler:

    #using reader function to read file and separate values by commas
    csvreader = csv.reader(file_handler, delimiter=",")

    #getting the header of the file and going to row 2
    hearder = next(csvreader)

    #preparing to count rows since they contain months information
    month_counter = 0

    #setting up profits counter
    profits_counter = 0

    #setting up profit change list to store all of the profit changes
    profit_change_list = []
    profit_change_dates = []

    #Set up total profit change to use for average calculation
    total_profit_change = 0

    #Grab first row to avoid including it in the profit change change
    first_row = next(csvreader)
    #Add 1 to the month counter since we skipped the second row
    month_counter += 1

    profits_counter += int(first_row[1])
    previous_row_profits = int(first_row[1])

    

    #Loop through the rows
    for row in csvreader:

        #----------------------------------------------------------------------------------------------------------
        #1. CALCULATE HOW MANY MONTHS OF DATA

        #   Add one to the month counter
        month_counter += 1

        #----------------------------------------------------------------------------------------------------------
        #2. CALCULATE TOTAL PROFIT/LOSS

        #   set up variable to hold profits of each row
        row_profits = int(row[1])
        #   Add the profits of each row to the total profits/losses counter
        profits_counter += row_profits

        #----------------------------------------------------------------------------------------------------------
        #3. FIND THE CHANGES IN PROFIT/LOSSES OVER THE ENTIRE PERIOD AND ADD THEM TO LIST

        #calculate profit change
        profit_change = row_profits - previous_row_profits
        #append the change to the list
        profit_change_list.append(profit_change)
        #get the date
        row_date = row[0]
        #append date to empty lis
        profit_change_dates.append(row[0])
        
        #Set this row's profit as previous profit for calculations with next row
        previous_row_profits = int(row[1])


#Calculate total profit change outside of for loop because the list is outside

for item in range(0, len(profit_change_list)):
    total_profit_change = total_profit_change + profit_change_list[item]

#calculate average profit change

average_profit_change = total_profit_change / len(profit_change_list)

# find greates increase in profit using max function
max_profit_increase = max(profit_change_list)
# get index to find the date
max_profit_increase_index = profit_change_list.index(max_profit_increase)
# get date using index to pull from dates list
max_profit_increase_date = profit_change_dates[max_profit_increase_index]

#find greatest decrease in profit using min function
max_profit_decrease = min(profit_change_list) 
# get index to find the date
max_profit_decrease_index = profit_change_list.index(max_profit_decrease)
# get date using index to pull from dates list
max_profit_decrease_date = profit_change_dates[max_profit_decrease_index]


Output = (
"Fiancial Analysis\n"
"---------------------------------------\n"
f'Total Months: {month_counter}\n'
f'Total: {profits_counter}\n'
f'Average Change: {average_profit_change}\n'
f'Greates increase in profits: {max_profit_increase_date} {max_profit_increase}\n'
f'Greates decrease in profits: {max_profit_decrease_date} {max_profit_decrease}\n'
)

print(Output)
    
with open(output_csvpath, "w") as new_document:
    new_document.write(Output)
