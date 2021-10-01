import csv

f_loc = 'data/elderlyBMI.tsv'
f_hand = open(f_loc, 'r')
reader = csv.reader(f_hand, delimiter = '\t')
header = next(reader)

print(header[0], header[1], header[4])

for ln in reader:
    if reader[3] != '':
        print(ln)
        #print(ln[0], int(ln[1]), "%.2f" % float(ln[4])) # print required fields

f_hand.close()
