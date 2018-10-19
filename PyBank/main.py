#Homework 3:Python PyBank 
#create a Python script that analyzes the records to calculate each of the following:
##The total number of months included in the dataset
##The total net amount of "Profit/Losses" over the entire period
##The greatest increase in profits (date and amount) over the entire period
##The greatest decrease in losses (date and amount) over the entire period
## In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Import CSV
import csv
import os 

#Files to load and output 
loadfile = os.path.join("raw data", "budget_data.csv")
outfile = os.path.join("analysis", "PyBank.txt")

#variables
date = []
profit_losses = []
greatest_increase = 0
greatest_inc_month = 0
greatest_decrease = 0
greatest_dec_month = 0

#open CSV file
with open(loadfile, newline = "") as bankdata:
    readcsv = csv.reader(bankdata, delimiter = ",")
    header = next(readcsv)

#total number of months included in dataset 
    for row in readcsv:
        date.append(row[0]) #add values to list 
        total_months = len(date)
    #print(count_months) #to check if code works

#total net amount of "Profit/Losses" over the entire period 
        profit_losses.append(int(row[1]))
        total_net_amount = sum(profit_losses)
    #print(total_net_amount) #to check if code works  

#greatest increase in profits (date & amount) over the entire period
        if greatest_increase > int(row[1]):
            greatest_increase
            greatest_inc_month

        else:
            greatest_increase = int(row[1])
            greatest_inc_month = row[0]

        if greatest_decrease < int(row[1]):
            greatest_decrease
            greatest_dec_month

        else:
            greatest_decrease = int(row[1])
            greatest_dec_month = row[0]
    
      
#Print Output to terminal 
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net_amount)}")
print(f"Greatest Increase in Profits: {str(greatest_inc_month)} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {str(greatest_dec_month)} (${str(greatest_decrease)})")

#export a text file with results 
#this printed but format was off
with open(outfile, "w", newline ="") as textfile:
    print("Financial Analysis", file = textfile,) 
    print("-------------------", file = textfile)
    print(f"Total Months: {str(total_months)}", file = textfile)
    print(f"Total: ${str(total_net_amount)}", file = textfile)
    print(f"Greatest Increase in Profits: {str(greatest_inc_month)} (${str(greatest_increase)})", file = textfile)
    print(f"Greatest Decrease in Profits: {str(greatest_dec_month)} (${str(greatest_decrease)})", file = textfile)