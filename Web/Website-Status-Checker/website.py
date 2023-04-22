# This Python script checks if a website is online and whether the heartbeat phrase is found. 
import requests
import csv


with open('db.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=";")

    for row in csvreader: 
        url = row[0]
        heartbeat = row[1]
        r = requests.get(f'{url}')

        if r.status_code == 200: 
            print (f'{url}is alive. Checking heearbeat code.')

            if  heartbeat in r.text: 
                print (f"{url} heartbeat found.")
            else:
                print ("Heartbeat not found. Check DB connection.")
        else: 
            print (f('{url} appears to be down.'))
