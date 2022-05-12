import os
import csv

election_data_csv = os.path.join('Resources\election_data.csv')
#make an file for the results to print out to.
election_results = os.path.join("analysis", "election_results.csv")

candidate= []
count_votes =0
results =[]
votes = []
percentage =[]
count_candidate =0




with open(election_data_csv, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
   # print(f"Header: {csv_header}")
   # Header: ['Ballot ID', 'County', 'Candidate']


with open(election_data_csv, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        candidate.append(row[2])
        count_votes += 1

        for x in set(candidate):
            results.append(x)
            votes.append(candidate.count(x))
            percentage.append((candidate.count(x)/count_votes)*100)
            count_candidate +=1

with open(election_results, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print("-----------------------------------", file=textfile)
    print(f'Total Votes: {count_votes}', file=textfile)
    print("-----------------------------------", file=textfile)
    for i in range(count_candidate):
        print(f'{results[i]}: {round(percentage[i], 2)}% ({votes[i]})', file=textfile)
    print("-----------------------------------", file=textfile)
    winner = results[votes.index(max(votes))]
    print(f'Winner: {winner}', file=textfile)
    print("-----------------------------------", file=textfile)


  
       


       



