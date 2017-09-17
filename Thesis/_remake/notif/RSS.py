import feedparser
import csv

feed = feedparser.parse('https://news.google.com/news/rss/headlines/section/q/bdo%20unibank/bdo%20unibank?ned=us&hl=en', '')
title = feed['entries'][1].title
url = feed['entries'][1].link
date = feed['entries'][1].updated
posts = []
for i in range(0,len(feed['entries'])):
    posts.append({
        'title': feed['entries'][i].title,
        'url': feed['entries'][i].link,
        'pubDate':feed['entries'][i].updated
    })
print(posts)
with open('RSSfeed.csv', 'w', ) as csvfile:
    fieldnames = ['pubDate','title', 'url']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, dialect = 'excel')
    writer.writerows(posts)

