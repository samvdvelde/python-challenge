import os
import csv

#Path to budget_data 

election_csv = os.path.join('Resources','election_data.csv')

with open(election_csv,'r') as csvfile:

    #Split the data over commas

    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore header

    next(csvreader)

    #List candidates with votes

    CandList = []
    TotalCandList = []

    for row in csvreader:

        #Make list of candidates
        TotalCandList.append(row[2])

        #Fill CandList with unique names
        if row[2] not in CandList:

            CandList.append(row[2])
        
            
    
    

    #Count votes for each candidate

    Cand1 = 0
    Cand2 = 0
    Cand3 = 0
    Cand4 = 0
    CandCount = []

    for i in TotalCandList:
        if i == CandList[0]:
            Cand1 += 1
        
        elif i == CandList[1]:
            Cand2 += 1

        elif i == CandList[2]:
            Cand3 += 1

        elif i == CandList[3]:
            Cand4 += 1
    
    CandCount.append(Cand1)
    CandCount.append(Cand2)
    CandCount.append(Cand3)
    CandCount.append(Cand4)

    print(CandCount)
        



    #for row in csvreader:
        #if row[2] == str('Khan'):
           # Khan += 1
        
    #print(Khan)
        
        #elif row[2] == str(CandList[1]):
            #Cand2 += 1
        
        #elif row[2] == str(CandList[2]):
            #Cand3 += 1

        #elif row[2] == str(CandList[3]):
            #Cand4 += 1
    
    #print(Cand1)
    #print(Cand2)
    #print(Cand3)
    #print(Cand4)


    


