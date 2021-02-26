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

    for row in csvreader:
        PLlist.append(row[1])

    
    #Split Profit/Loss List over even and odd indices to calculate change
    PLodd = PLlist[::2]
    PLeven = PLlist[1::2]

    #Need to eliminate first element of the odds list to generate second list of changes
    PLodd2 = PLodd.copy()
    PLodd2.pop(0)

    

    #create even-odd change lists
    EminO = []
    OminE = []
    for even, odd in zip(PLeven, PLodd):
        ChangeEO = int(even) - int(odd)
        EminO.append(ChangeEO)

    for odd, even in zip(PLodd2, PLeven):
        ChangeOE = int(odd) - int(even)
        OminE.append(ChangeOE)

    #Append 0 to Odd minus Even change list to have same amount of values in both Odd minus Even and Even minus Odd lists.
    #This is important when we merge with zip as the last value won't be excluded.

    OminE.append(0)

    
    #Merge the change lists into a full change list

    ChangeZip = zip(EminO,OminE)

    # Convert zip to list 

    ChangeList = []

    for i in ChangeZip:
        for j in i:
            ChangeList.append(j)

    #Remove 0 again from ChangeList

    ChangeList2 = ChangeList.copy()

    ChangeList2.pop()


        

    print(ChangeList2)
    

    

        







    

    






