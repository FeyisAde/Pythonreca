import csv

sales = open('sales.csv','r')
csv_file = csv.reader(sales,delimiter=',')
outfile = open('salesreportFINAL.csv','w')
outfile.write('CustomerID,Total\n')

next(csv_file)

totals_by_ID = {}

for row in csv_file:
    customerID = row[0]
    total = float(row[3]) + float(row[4]) + float(row[5])

    # Aggregate (sum) totals per customerID
    if customerID in totals_by_ID:
        totals_by_ID[customerID] += total
    else:
        totals_by_ID[customerID] = total

 # Write each customer once (sorted by customer ID)
for customerID in sorted(totals_by_ID):
    outfile.write(f"{customerID},{totals_by_ID[customerID]:.2f}\n")     

outfile.close()

