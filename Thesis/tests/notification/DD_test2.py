import urllib3

url = 'http://edge.pse.com.ph/companyDisclosures/form.do?cmpy_id=651'
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET', url)

print (r.data.encode('utf-8'))