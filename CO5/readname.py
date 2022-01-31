import csv
filename = "names.csv"
cf=open(filename, 'r') 
#csvreader = csv.reader(cf)
data = csv.DictReader(cf)
print("No         Company")

for r in data:
 
                print(r['No'], r['Company'])
