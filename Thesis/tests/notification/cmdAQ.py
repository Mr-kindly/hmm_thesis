import requests
from HTMLParser import HTMLParser

body_found = False
msg = ""


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if str(tag) == 'body':
            global body_found
            body_found = True

    def handle_endtag(self, tag):
        if str(tag) == 'body':
            global body_found
            body_found = False

    def handle_data(self, data):
        if body_found:
            global msg
            msg = data


def command_acquire(url):

    response = requests.get(url)
    html = response.content
    parser = MyHTMLParser()
    parser.feed(html)
    return msg.strip()
