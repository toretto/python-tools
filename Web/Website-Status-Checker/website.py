# This Python script checks if a website is online and whether the heartbeat phrase is found. 
from re import X
import requests
import csv
import socket

class bcolors:
    SUCC = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\x1b[31m'

print("\nStarting host scans. \n")
print("#RESULTS \n")

with open('db.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=";")

    for row in csvreader: 
        hostname = row [0]
        url = row[1]
        heartbeat = row[2]
        try:
            o = socket.gethostbyname(hostname)
        except:
            print (f"{bcolors.FAIL}Can\'t resolve the hostname {hostname}, skipping.{bcolors.ENDC}\n")
            continue
        r = requests.get(f'{url}')
        # print (r.status_code)
        if r.status_code == 200: 
            print (f'{bcolors.SUCC}{url} is alive. Checking heearbeat code.{bcolors.ENDC}')

            if  heartbeat in r.text: 
                print (f"{bcolors.SUCC}{url} heartbeat found. {bcolors.ENDC}\n")
            else:
                print (f"{bcolors.FAIL}Heartbeat not found. Check DB connection.{bcolors.ENDC} \n")
        else: 
            print (f"{bcolors.FAIL}{url} appears to be down.\nNo heartbeat for obvious reasons.{bcolors.ENDC}")