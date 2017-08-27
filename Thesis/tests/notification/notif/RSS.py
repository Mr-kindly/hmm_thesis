import feedparser
import csv
#
feed = feedparser.parse('https://news.google.com/news/rss/headlines?hl=en&ned=us')#joke site lang to, tinry ko lang
title = feed['entries'][1].title
url = feed['entries'][1].link
date = feed['entries'][1].updated
posts = []
for i in range(0, len(feed['entries'])):
    posts.append({
        'title': feed['entries'][i].title,
        'url': feed['entries'][i].link,
        'pubDate':feed['entries'][i].updated
    })

with open('RSSfeed.csv', 'w') as csvfile:
    fieldnames = ['pubDate','title', 'url']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, dialect = 'excel')
    writer.writeheader()
    writer.writerows(posts)

print('notification acquired')