from xml.dom import minidom
import requests
nyt_rss = "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml"

r = requests.get(nyt_rss, verify = False)

print(r.text)



