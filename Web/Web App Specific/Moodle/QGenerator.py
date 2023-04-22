import csv
import sys

counter = 1

with open('examentestv2.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')
    for row in csvreader:
        with open('export.txt', 'a') as f:
            sys.stdout = f 
            Q = row[0];
            true = row[1];
            false = row[2];
            truecomment = row[3];
            falsecomment = row[4];
            print(f" // Question {counter}")
            print (f'::Q{counter}:: {row[0]}')
            print (f"{{={true} # {truecomment} ~{false} # {falsecomment}}}")
            print()
            counter += 1
