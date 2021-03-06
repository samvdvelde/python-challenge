import os
import csv

#Path to budget_data 

election_csv = os.path.join('Resources','election_data.csv')

with open(election_csv,'r') as csvfile:

    #Split the data over commas

    csvreader = csv.reader(csvfile, delimiter=',')

    #Ignore header

    next(csvreader)





    #Set variables for candidates and vote counts

    CandList = []
    TotalCandList = []
    TotalVoters = 0
    Cand1 = 0
    Cand2 = 0
    Cand3 = 0
    Cand4 = 0
    CandCount = []
    VotePct = []

    for row in csvreader:

        #Calculate total voters
        TotalVoters += 1

        #Make list of candidates
        TotalCandList.append(row[2])

        #Fill CandList with unique names
        if row[2] not in CandList:

            CandList.append(row[2])
        
            
    #Count votes for each candidate
    
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

    #Calculate vote percentages

    for i in CandCount:
        Pct = round(float(float(i)/float(TotalVoters) * 100),3)
        VotePct.append(Pct)

    #Get winner
    Winner = CandList[CandCount.index(max(CandCount))]
  
    print('`````')
    print('Election Results')
    print('-----------------------')
    print('Total Votes: ' + str(TotalVoters))
    print('-----------------------')
    for cand, pct, count in zip(CandList, VotePct, CandCount):
        print('{}: {}% ({})'.format(cand, pct, count))
    print('-----------------------')
    print('Winner: ' + str(Winner))
    print('-----------------------')
    


# Path to analysis
output_file = os.path.join("analysis", "PyPoll.txt")


# Open the file using "write" mode.
with open(output_file,'wb') as PyPoll:


    # Initialize csv.writer
    csvwriter = csv.writer(PyPoll, delimiter=',')


    # Write the rows
    csvwriter.writerow(['`````'])
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Total Votes: ' + str(TotalVoters)])
    csvwriter.writerow(['-----------------------'])
    for cand, pct, count in zip(CandList, VotePct, CandCount):
        csvwriter.writerow(['{}: {}% ({})'.format(cand, pct, count)])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Winner: ' + str(Winner)])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['`````'])

