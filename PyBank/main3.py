import os
import csv

#Path to budget_data 

budget_csv = os.path.join('Resources','budget_data.csv')

with open(budget_csv,'r') as csvfile:

    #Split the data over commas

    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore header

    next(csvreader)


    #Sum up profit/loss and create list with all profit/loss values

    SumPL = 0
    PLlist = []
    Changelist = []
    TotalMonths = 0
    Monthlist = []
    
 
    
    for row in csvreader:
        TotalMonths += 1
        SumPL += int(row[1])
        PLlist.append(int(row[1]))
        Monthlist.append(str(row[0]))

    for i in range(len(PLlist) - 1):
        Change = PLlist[i+1] - PLlist[i]
        Changelist.append(Change)


    
    #Find months with max increase and max decline

    MaxIncMonth = Monthlist[Changelist.index(max(Changelist)) + 1]

    MaxDecMonth = Monthlist[Changelist.index(min(Changelist)) + 1]

 

    #Calculate Average change

    AverageChange = round(sum(Changelist) / len(Changelist), 2)


    #Find greatest increase in profit

    MaxProfInc = max(Changelist)


    #Find greatest decrease in profit

    MaxProfDec = min(Changelist)

    print('`````')
    print('Financial Analysis')
    print('-----------------------')
    print('Total Months: ' + str(TotalMonths))
    print('Average Change: $' + str(AverageChange))
    print('Greatest Increase in Profits: ' + str(MaxIncMonth) + ' $' + '(' + str(MaxProfInc) + ')')
    print('Greatest Decrease in Profits: ' + str(MaxDecMonth) + ' $' + '(' + str(MaxProfDec) + ')')
    print('`````')






   