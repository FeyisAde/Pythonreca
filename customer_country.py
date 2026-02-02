import csv

customers = open('customers.csv','r')

csv_file = csv.reader(customers,delimiter=',')

outfile = open('customer_country.csv','w')

outfile.write('Full Name,Country\n')

next(csv_file)

# Counter for total customers
customer_count = 0

for row in csv_file:
    name = row[1] + ' ' + row[2]
    country = row[4]

    outfile.write(name + ',' + country + '\n')

    # Increment count for each customer read
    customer_count += 1

outfile.close()    