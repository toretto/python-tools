# This Python script checks if a website is online and whether the Heartbeat phrase is found. 
from re import X
import requests
import csv
import socket
import smtplib, ssl
from email.message import EmailMessage

cronmode = 0

class bcolors:
    SUCC = '\033[92m'
    ENDC = '\033[0m'
    FAIL = '\x1b[31m'

print("\nStarting host scans. \n")
print("#RESULTS \n")

content = "<h2>Website Status Report</h2>"
content += "<p>Below are the results of the website status check:</p>"

# IMPORTANT: Replace dv.csv with the full path when using Cronjobs!
with open('db.csv') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=";")

    for row in csvreader: 
        hostname = row [0]
        url = row[1]
        Heartbeat = row[2]
        try:
            o = socket.gethostbyname(hostname)
        except:
            print (f"{bcolors.FAIL}Can\'t resolve the hostname {hostname}, skipping.{bcolors.ENDC}\n")
            continue
        r = requests.get(f'{url}')
        # print (r.status_code)
        if r.status_code == 200: 
            print (f'{bcolors.SUCC}{url} is alive. Checking Heartbeat code. {bcolors.ENDC}')
            # Adding to Mail Content
            content += (f'<p>{url} is alive. Checking Heartbeat code. </p>')
            if Heartbeat == "":
                print ("No heartbeat in database, skipping.\n")
            else:
                if  Heartbeat in r.text:
                    print (f"{bcolors.SUCC}{url} Heartbeat found. {bcolors.ENDC}\n")
                    # Adding to Mail Content
                    content += (f"<p>{url} Heartbeat found.</p><br/>")
                else:
                    print (f"{bcolors.FAIL}Heartbeat not found. Please check your page and DB connection. {bcolors.ENDC} \n")
                    # Adding to Mail Content
                    content += (f"<p>Heartbeat not found. Please check your page and DB connection. </p><br/>")
        else: 
            print (f"{bcolors.FAIL}{url} appears to be down.\nNo Heartbeat for obvious reasons. {bcolors.ENDC}")
            # Adding to Mail Content
            content += (f"<p><strong><em>{url} appears to be down. No Heartbeat for obvious reasons. </p></strong></em>")

# print ("Testing Mail Content \n")
# print (content)

# initialize connection to our email server.
smtp = smtplib.SMTP('mail.example.com', port='587')

smtp.ehlo()  # send the extended hello to our server
smtp.starttls()  # tell server we want to communicate with TLS encryption

smtp.login('email@example.com', 'Password')  # login to our email server

# Setting Message Content
msg = EmailMessage()
#Define the message and send as HTML
msg.set_content(content, subtype='html')
# Define the subject of the email
msg['Subject'] = "Website Status Report"

# send our email message 'msg' to our boss
smtp.sendmail("automailer@qfirst.dev","steven@qfirst.dev",msg.as_string())
              
smtp.quit()

print ("Message sent!")  # finally, don't forget to close the connection