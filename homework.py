import csv

f_hand = open('data/nhanes.csv', 'r')
out_file = open('data/nhanes_bmi.tsv', 'w')

reader = csv.reader(f_hand, delimiter='\t')
writer = csv.writer(out_file, delimiter='\t')

header =  next(reader)
header.append('BMI')
writer.writerow(header)

counter = 0
na_count = 0
indiv = []
age = []
sex = []
weight  = []
height = []

for ind, aj, sx, wgt, ht in reader:
    counter = counter + 1

    if wgt == 'NA' or ht == 'NA':
        na_count = na_count+1
        continue
    indiv.append(ind)
    sex.append(sx)
    age.append(aj)
    weight.append(wgt)
    height.append(ht)

m_count = 0
for i in range(len(sex)):
    if int(sex[i]) == 1:
        m_count = m_count+1
f_count = len(sex)-m_count

print('There are %d rows of data.' % counter)
print('There are %d males and %d females in the dataset.' % (m_count, f_count))
print('There are %d NA values for height and weight in the dataset' % na_count)

bmi = []

for i in range(len(weight)):

    bmi.append(float(weight[i]) / (float(height[i])/100)**2)

data_out = zip(indiv, age, sex, weight, height, bmi)
for row in data_out:
    writer.writerow(row)

m_bmi = []
f_bmi = []

for i in range(len(sex)):
    if int(sex[i])==1:
        m_bmi.append(bmi[i])
    else:
        f_bmi.append(bmi[i])

ave_male = sum(m_bmi)/len(m_bmi)
ave_female = sum(f_bmi)/len(f_bmi)

print('The average male BMI is %.2f; the average female BMI is %.2f.' % (ave_male, ave_female))
