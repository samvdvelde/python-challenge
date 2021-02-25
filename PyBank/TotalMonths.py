import os
import csv

#Path to budget_data 

budget_csv = os.path.join('Resources','budget_data.csv')

with open(budget_csv,'r') as csvfile:

    #Split the data over commas

    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore header

    next(csvreader)


    #Calculate total months

    TotalMonths = len(list(csvreader))

    print(TotalMonths)