

#Path to BankSummary

BankSummary = os.path.join('analysis','BankSummary.txt')


# Open BankSummary
with open(BankSummary, "w", newline="") as datafile:
    writer = csv.writer(datafile)

