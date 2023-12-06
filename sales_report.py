"""Generate sales report showing total melons each salesperson sold."""


salespeople = []  # empty list
melons_sold = []  # empty list

f = open('sales-report.txt')  # opens .txt file

for line in f:  # looping over file data
    line = line.rstrip()  # removing any white space on the right
    # pipe is splitting different items and creates a list
    entries = line.split('|')
    # salesperson is first item of the list is asigned as variable
    salesperson = entries[0]
    # third item of the list is converted into integer and asigned as a variable
    melons = int(entries[2])

    if salesperson in salespeople:  # checking condition if salesperson is in the empti salespeople list
        # if he already is, then get the index of salesperson in salespeople list
        position = salespeople.index(salesperson)
        melons_sold[position] += melons  # sold +melons

    else:
        # if not in the list, then append salesperson to salespeople list
        salespeople.append(salesperson)
        melons_sold.append(melons)  # append sol melons


for i in range(len(salespeople)):  # looping over salespeople list
    # printing out salesperson sold ... melons
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
