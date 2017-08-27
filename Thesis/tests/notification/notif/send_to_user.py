# For notification system, unfiltered

import fbchat
import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=True, help="Username of the sender")
ap.add_argument("-p", "--password", required=True, help="Password")
ap.add_argument("-r", "--receiver", required=True, help="Receiver's full name")
args = vars(ap.parse_args())


client = fbchat.Client(args["username"], args["password"])
with open("RSSfeed.csv", 'rb') as csvfile:
    RSSfeed = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in RSSfeed:
        sent = client.send(args["receiver"], ' '.join(row))
        print (' '.join(row))

if sent:
    print("Message sent successfully!")
