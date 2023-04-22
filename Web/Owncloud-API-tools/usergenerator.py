import requests
import owncloud


with open(filepath) as s: 
    lineslist = s.readlines()
    
    for line in lineslist:
        # The URL for your Owncloud instance, E.G https://mywebsite.com/owncloud/
        owncloudInstanceURL = "https://example.com"
        # The default password, this will be used by all users in the list
        defaultPassword = "examplePassword"
        # The location of the file containing the usrnames
        filepath = "fileLocation"
              
        # Accesssing the API
        oc = owncloud.Client('{}'.format(owncloudInstanceURL))
        # oc.login("{}".format(adminLogin), "{}".format(adminPassword))
        
        # As much as I hate it, this library hates you and requires you to use your username and password below
        oc.login("yourUsername", "yourPassword")
        userName = line.strip()
        oc.create_user("{}".format(userName),"{}".format(defaultPassword))
        # You can commment out the values below, if you feel like it
        print (userName)
        print (defaultPassword)