import fbchat
import csv


client = fbchat.Client("drexcalibara95@gmail.com", "Rickshaw72197")
friends = client.getUsers("Daniel Cabrales")  # return a list of names
friend = friends[0]

with open('C:\Users\Agent Orange\PycharmProjects\Thesis\Notif\RSSfeed.csv', 'rb') as csvfile:
    RSSfeed = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
    for row in RSSfeed:
        sent = client.send(friend.uid, ' '.join(row))

if sent:
    print("Message sent successfully!")




