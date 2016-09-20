import os
os.chdir('/Users/jordanawan/Desktop/Kaggle_Bosch')

import csv
#below is a way to read one line at a time without reading the whole file
#into memory.
'''with open('train_date.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
'''
#begin a timer
t0 = time.time()
#the below can count the number of lines in a file.
#There are about 1million lines in train_date.csv
'''
count = 0;
for line in open('train_date.csv'):
    count+=1;
#t1 = time.time()
print('total number of lines')
print(count)
'''
#This section is used to make the smaller versions of the files. I did one at a
#time and just modified the code.

with open('train_date.csv') as myfile:
    csvReader1 = csv.reader(myfile)

#add a row at a time to head
    head = []
    for x in range(0,501):
         head.append(next(csvReader1))
#write head to the file, one line at a time.
writer = csv.writer(open("baby_train_date.csv", 'w'))
for row in head:
    writer.writerow(row)





t1 = time.time()
#print(count)
print(t1-t0)
