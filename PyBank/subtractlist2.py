import os
import csv

#Path to budget_data 

budget_csv = os.path.join('Resources','budget_data.csv')

with open(budget_csv,'r') as csvfile:

    #Split the data over commas

    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore header

    next(csvreader)




    #Make list with all Profit/Loss values
    
    PLlist = []
    Changelist = []

    for row in csvreader:
        PLlist.append(int(row[1]))

    for i in range(len(PLlist) - 1):
        Change = PLlist[i+1] - PLlist[i]
        Changelist.append(Change)
    print(PLlist)
    print(Changelist)    

        

   

