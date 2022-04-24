from calendar import month
import os
import csv
import statistics

budget_data_csv = os.path.join("..", "PyBank", "budget_data.csv")

months =[]
months = 0
net_profit = []
net_profit = 0
total_average =0
great_gain =0
great_loss =0
great_month =0
worst_month=0

with open(budget_data_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
   
    for row in csv_reader:
       
        months += 1
        net_profit += int(row[1])
        
        #input the value for the greatest gain in the time
        if int(row[1]) > great_gain:
            
            great_gain=int(row[1])
        elif int(row[1]) < great_loss:
            
            great_loss=int(row[1])

        months.append(int(row[1]))

    
        
            