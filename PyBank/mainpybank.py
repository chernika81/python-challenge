# Modules
import os
import csv

# Define the path of the csv file
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")


# Defining the variables
total_months = 0
profit_loss = 0
net_total_profit_loss = 0
month_before_profit_loss = 0
change = 0
greatest_increase = 0
greatest_decrease = 0




# Make lists to store column values
date = []
change_total = []
greatest_increase_month = "None"
greatest_decrease_month = "None"

change =[]




# Open the csv with the csv.reader
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


    # Header
    csv_header = next(csvfile)

    # Counting the total for date column
    change = 0
    for row in csv_reader:
        total_months += 1
       

        # Finding the total for profit/losses column
        profit_loss = int(row[1])
        net_total_profit_loss += profit_loss

        
        # opening a loop to find the change in profit and loss
        
        if (total_months ==1):
            month_before_profit_loss = profit_loss
            continue
        
        else:
            change = profit_loss - month_before_profit_loss  
            
            date.append(row[0])
            change_total.append(change)
        
            month_before_profit_loss = profit_loss
            
        
        

    # Finding the totals for the average calculation       
        
    sum_change_total = sum(change_total)
    ave_change_total = round(sum_change_total/(total_months - 1), 2)


# Finding the greatest increase in profits and greatest decrease in profits
    
    greatest_increase_month = "None"
    greatest_decrease_month = "None"
    
    for change in change_total:
        if change > greatest_increase:
            greatest_increase = change
            change_index = change_total.index(change)
            greatest_increase_month = date[change_index]

    
    for change in change_total:
        if change < greatest_decrease:
            greatest_decrease = change
            change_index = change_total.index(change)
            greatest_decrease_month = date[change_index]
    




# Terminal printing
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_profit_loss}")
print(f"Average Change: ${ave_change_total}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Text file printing. Defining a path to the output file
output_file = os.path.join("/Users/arminearutyunyan/Desktop/PythonStuff/output/output_pybank.txt")
with open(output_file, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total_profit_loss}\n")
    txt_file.write(f"Average Change: ${ave_change_total}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")




    
        


         
                                



    














        

    


