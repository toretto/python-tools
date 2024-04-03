#Instructions
- Create a file named "db.csv" in the folder
- If required, install the requests library > pip install requests
- 
# Add sites to the CSV, one per line
- Column 1: the hostname, e.g examplesite.com
- Column 2: the site's full URL, e.g https://examplesite.com
- Column 3: the "heartbeat", a snippet of text that can be found on the front page.

# E-mail settings
- Change the e-mail settings by providing a valid hostname, username and password. This version currently assumes your mail server supports TLS.
- Contact us if that doesn't work for you and we can update the script accordingly!

# Run the script

# Running as Cronjob
- To run the script as a cronjob, you'll need to provide the full path to db.csv e.g /home/hackerman/scripts/websitechecker/db.csv.
