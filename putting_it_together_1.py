import csv

f_hand = open('data/elderlyHeightWeight.csv', 'r')
bmi_data = open('data/elderlyBMI.tsv', 'w')

writer = csv.writer(bmi_data, delimiter = '\t')
reader = csv.reader(f_hand, delimiter = '\t') 

header = next(reader)
header.append('BMI')
writer.writerow(header)

sex = []
age = []
weight  = [] 
height = []

for sx, aj, wgt, ht in reader:
    sex.append(sx)
    age.append(aj)
    weight.append(wgt)
    height.append(ht)

bmi = []

for i in range(len(weight)):
    bmi.append(float(weight[i]) / (float(height[i])/100)**2)

data_out = zip(sex, age, weight, height, bmi)

for row in data_out:
    writer.writerow(row)
    
bmi_data.close()
f_hand.close()
