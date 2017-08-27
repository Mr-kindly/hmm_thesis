from lxml import html
import requests

url = 'http://edge.pse.com.ph/companyDisclosures/form.do?cmpy_id=651'
response = requests.get(url)
ss = response.content
print ss