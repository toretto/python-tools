import csv
import sys
import os

counter = 1
filename = sys.argv[1]

print(filename)

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')
    for row in csvreader:
        S = row[0];
        os.system(f"start msedge {S}")