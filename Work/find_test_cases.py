import csv
import sys

train_addr = 'New_Dataset.csv'
test_addr = 'sequences_test.csv'


Trains = []
Tests = []




train_file = open(train_addr)
line = train_file.readline()
line = train_file.readline()
while line:
    line = line.rstrip('\n')
    linespl = line.split(',')
    Trains.append(linespl[0])
    line = train_file.readline()



test_file = open(test_addr)
line = test_file.readline()
line = test_file.readline()
while line:
    line = line.rstrip('\n')
    linespl = line.split(',')
    Tests.append(linespl[0])
    line = test_file.readline()

test_set = set(Tests)
train_set = set(Trains)

rem = train_set-test_set


s = 5
s = 3
s = 7