from calendar import month
import os
import csv
import statistics

budget_data_csv = os.path.join("..", "PyBank", "budget_data.csv")

months =[] #The total number of months included in the dataset
months = 0
net_profit = [] #The net total amount of "Profit/Losses" over the entire period
net_profit = 0
previous_month =0
current_month =0
total_average =0 # the average of those changes
great_profit =0
great_loss =0


with open(budget_data_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
   
    for row in csv_reader:
       
        months += 1
        
        great_month = int(row[1])
        net_profit += great_month

        if months == 1:
            previous_month =current_month

        else:
            net_profit = current_month - previous_month
            months.append(row[1])
            net_profit.append(net_profit)
            previous_month = current_month
        
total_net_profit = sum(net_profit)
total_average = (total_net_profit/months)

great_profit = max(net_profit)
great_loss = min(net_profit)

great_month_index = net_profit.index(highest_change)
low_month_index = net_profit.index(lowest_change)
        
high_month = months[great_month_index]
low_month = months[low_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${total_average}")
print(f"Greatest Increase in Profits:  {high_month} (${great_profit})")
print(f"Greatest Decrease in Losses:  {low_month} (${great_loss})")

budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {months}\n")
    outfile.write(f"Total:  ${net_profit}\n")
    outfile.write(f"Average Change:  ${total_average}\n")
    outfile.write(f"Greatest Increase in Profits:  {high_month} (${great_profit})\n")
    outfile.write(f"Greatest Decrease in Losses:  {low_month} (${great_loss})\n")

        
            