# This Python script checks if a website is online and whether the heartbeat phrase is found. 
import requests

url = "https://stevenzeegers.me"
r = requests.get(f'{url}')

if r.status_code == 200: 
    print (f'{url}is alive. Checking heearbeat code.')

    if "Steven Blogs" in r.text: 
        print (f"{url} heartbeat found.")
    else:
        print ("Heartbeat not found. Check DB connection.")
else: 
    print (f('{url} appears to be down.'))
