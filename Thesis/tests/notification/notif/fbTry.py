import fbchat
import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-u')

client = fbchat.Client('rockport_mw20@yahoo.com', 'Permittivity8.85E-12')


with open("RSSfeed.csv", 'rb') as csvfile:
    RSSfeed = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
    for row in RSSfeed:
        sent = client.send(1540864023, ' '.join(row) )
        print (' '.join(row))


if sent:
    print("Message sent successfully!")




